from typing import List

from django.db.models import Count, Exists, OuterRef, Q
from rest_framework import exceptions

from books.models import Bookmark
from books.models.book import Book
from books.models.repositories.serializers.books_repo_srl import BooksRepoListVLD
from goodreads.utils.pagination import paginate_queryset
from users.models import User


class BooksRepo:
    def __init__(self, requester: User):
        self.requester = requester

    @paginate_queryset(params_field='params')
    def list(self, params) -> List[Book]:
        params_vld = BooksRepoListVLD(data=params)
        params_vld.is_valid(raise_exception=True)

        query = Q()

        queryset = Book.objects.filter(query).annotate(
            bookmark_count=Count('bookmarks'),
        )

        if self.requester.is_authenticated:
            bookmarks_subquery = Bookmark.objects.filter(
                user=self.requester,
                book=OuterRef('pk'),
            )

            queryset = queryset.annotate(
                is_bookmarked=Exists(bookmarks_subquery),
            )

        return queryset

    def retrieve(self, book_id: str) -> Book:
        query = Q(id=book_id)

        try:
            return Book.objects.filter(query).get()
        except Book.DoesNotExist:
            raise exceptions.NotFound('Book not found.')
