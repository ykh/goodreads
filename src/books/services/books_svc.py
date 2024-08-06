from typing import List

from rest_framework import exceptions

from books.models.book import Book
from books.models.repositories.books_repo import BooksRepo
from books.services.serializers.books_svc_srl import BooksSVCListVLD
from goodreads.utils.singleton import singleton
from goodreads.utils.validators import validate_uuid
from users.models import User


@singleton
class BooksService:

    def list(self, params, requester: User) -> List[Book]:
        params_vld = BooksSVCListVLD(data=params)
        params_vld.is_valid(raise_exception=True)

        books_repo = BooksRepo(requester=requester)

        return books_repo.list(params=params_vld.validated_data)

    @validate_uuid(
        'book_id',
        exception=exceptions.ValidationError,
        message='Given book id is not valid.',
        is_optional=False,
    )
    def retrieve(self, book_id: str, requester: User) -> Book:
        books_repo = BooksRepo(requester=requester)

        return books_repo.retrieve(book_id=book_id)
