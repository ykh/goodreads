from rest_framework import exceptions

from goodreads.utils.singleton import singleton
from goodreads.utils.validators import validate_uuid
from reviews.models import Review
from reviews.models.repositories.reviews_repo import ReviewsRepo
from reviews.services.serializers.reviews_svc_srl import (
    ReviewsSVCCreateVLD,
    ReviewsSVCUpdateVLD,
)
from users.models import User


@singleton
class ReviewsService:
    def create(self, params, requester: User) -> Review:
        params_vld = ReviewsSVCCreateVLD(data=params)
        params_vld.is_valid(raise_exception=True)

        v_data = params_vld.validated_data

        reviews_repo = ReviewsRepo(requester=requester)

        return reviews_repo.create(
            params=params_vld.validated_data,
            user_id=v_data['user_id'],
            book_id=v_data['book_id'],
        )

    def update(self, params, requester: User) -> Review:
        params_vld = ReviewsSVCUpdateVLD(data=params)
        params_vld.is_valid(raise_exception=True)

        v_data = params_vld.validated_data

        reviews_repo = ReviewsRepo(requester=requester)

        review = reviews_repo.update(
            params=params_vld.validated_data,
            user_id=v_data['user_id'],
            book_id=v_data['book_id'],
        )

        return review
