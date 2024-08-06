from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from books.services.books_svc import BooksService
from books.views.serializers.books_view_srl import (
    BooksViewListTRF,
    BooksViewRetrieveTRF,
)
from goodreads.utils.pagination import paginate_view_response


class BooksViewSet(ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.books_svc = BooksService()

    @paginate_view_response(trf_class=BooksViewListTRF)
    def list(self, request):
        paginated_result = self.books_svc.list(
            params=request.query_params,
            requester=request.user,
        )

        return paginated_result

    def retrieve(self, request, pk):
        result = self.books_svc.retrieve(
            book_id=pk,
            requester=request.user,
        )

        return Response(
            BooksViewRetrieveTRF(instance=result).data,
            status=status.HTTP_200_OK,
        )
