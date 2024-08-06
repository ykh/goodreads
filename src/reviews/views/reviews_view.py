from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from reviews.services.reviews_svc import ReviewsService
from reviews.views.serializers.reviews_view_srl import (
    ReviewsViewCreateTRF,
    ReviewsViewUpdateTRF,
)


class ReviewsViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.reviews_svc = ReviewsService()

    def submit(self, request, book_id):
        review = self.reviews_svc.create(
            params={
                **request.data,
                'user_id': request.user.id,
                'book_id': book_id,
            },
            requester=request.user,
        )

        return Response(
            ReviewsViewCreateTRF(instance=review).data,
            status=status.HTTP_201_CREATED,
        )

    def resubmit(self, request, book_id):
        review = self.reviews_svc.update(
            params={
                **request.data,
                'user_id': request.user.id,
                'book_id': book_id,
            },
            requester=request.user,
        )

        return Response(
            ReviewsViewUpdateTRF(instance=review).data,
            status=status.HTTP_200_OK,
        )
