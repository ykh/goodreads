from django.db import transaction
from rest_framework import exceptions

from books.models import Book
from books.models.repositories.bookmarks_repo import BookmarksRepo
from reviews.models import Review
from reviews.models.repositories.serializers.reviews_repo_srl import (
    ReviewsRepoCreateVLD,
    ReviewsRepoUpdateVLD,
)
from users.models import User


class ReviewsRepo:
    def __init__(self, requester: User):
        self.requester = requester

    @transaction.atomic
    def create(self, params, user_id: str, book_id: str) -> Review:
        try:
            user = User.objects.get(id=user_id)
            book = Book.objects.get(id=book_id)
        except User.DoesNotExist:
            raise exceptions.NotFound('User not found.')
        except Book.DoesNotExist:
            raise exceptions.NotFound('Book not found.')

        params_vld = ReviewsRepoCreateVLD(
            data={
                **params,
                'user': user.id,
                'book': book.id,
            }
        )

        params_vld.is_valid(raise_exception=True)

        review = params_vld.save()

        bookmarks_repo = BookmarksRepo(requester=self.requester)

        bookmarks_repo.unbookmark_if_exists(user_id=user_id, book_id=book_id)

        return review

    @transaction.atomic
    def update(self, params, user_id: str, book_id: str) -> Review:
        try:
            user = User.objects.get(id=user_id)
            book = Book.objects.get(id=book_id)
            review = Review.objects.get(user=user, book=book)
        except User.DoesNotExist:
            raise exceptions.NotFound('User not found.')
        except Book.DoesNotExist:
            raise exceptions.NotFound('Book not found.')
        except Review.DoesNotExist:
            raise exceptions.NotFound('Review not found.')

        validator = ReviewsRepoUpdateVLD(data=params, instance=review, partial=True)
        validator.is_valid(raise_exception=True)

        review = validator.save()

        bookmarks_repo = BookmarksRepo(requester=self.requester)

        bookmarks_repo.unbookmark_if_exists(user_id=user_id, book_id=book_id)

        return review
