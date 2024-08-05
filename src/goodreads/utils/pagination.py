from functools import wraps

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from rest_framework import exceptions, serializers, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page_number'
    page_size_query_param = 'page_size'
    max_page_size = 100


def paginate_view_response(trf_class, status_code=status.HTTP_200_OK):

    def paginate_response(data, paginated_result):
        class PaginatedResponse(serializers.Serializer):
            result = serializers.ListField()
            count = serializers.IntegerField()
            total_pages = serializers.IntegerField()
            current_page = serializers.IntegerField()
            page_size = serializers.IntegerField()

        params_trf = PaginatedResponse(
            data={
                'result': data,
                'count': paginated_result.paginator.count,
                'total_pages': paginated_result.paginator.num_pages,
                'current_page': paginated_result.number,
                'page_size': paginated_result.paginator.per_page,
            }
        )

        params_trf.is_valid()

        return params_trf.validated_data

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            paginated_result = fn(*args, **kwargs)

            result = Response(
                paginate_response(
                    data=trf_class(
                        instance=paginated_result.object_list,
                        many=True,
                    ).data,
                    paginated_result=paginated_result,
                ),
                status=status_code,
            )

            return result

        return wrapper

    return decorator


def paginate_queryset(params_field: str):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                params = kwargs[params_field]
            except KeyError:
                raise exceptions.ValidationError(
                    'Field name must be passed to the paginate decorator',
                )

            queryset = fn(*args, **kwargs)

            page_number = params.get('page_number', 1)
            page_size = params.get('page_size', 10)

            if not queryset.query.order_by:
                queryset = queryset.order_by('id')

            paginator = Paginator(queryset, page_size)

            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)

            return page

        return wrapper

    return decorator
