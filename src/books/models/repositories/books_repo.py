from typing import List

from django.db.models import Avg, Count, Q
from rest_framework import exceptions

from books.models.book import Book
from books.models.repositories.serializers.books_repo_srl import BooksRepoListVLD
from goodreads.utils.pagination import paginate_queryset
from reviews.models import Review
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
            bookmark_count=Count('bookmarks')
        )

        return queryset

    def retrieve(self, book_id: str) -> [dict]:
        try:
            book = Book.objects.filter(id=book_id).get()
        except Book.DoesNotExist:
            raise exceptions.NotFound('Book not found.')

        further_info_queryset = Review.objects.filter(
            book=book,
        ).aggregate(
            comment_count=Count('comment', filter=~Q(comment='') & ~Q(comment=None)),
            rate_count=Count('rate'),
            average_rate=Avg('rate'),
            count_rate1=Count('rate', filter=Q(rate=1)),
            count_rate2=Count('rate', filter=Q(rate=2)),
            count_rate3=Count('rate', filter=Q(rate=3)),
            count_rate4=Count('rate', filter=Q(rate=4)),
            count_rate5=Count('rate', filter=Q(rate=5)),
        )

        reviews = Review.objects.filter(book=book).values(
            'comment',
            'rate',
        )

        result = {
            'id': book.id,
            'title': book.title,
            'summary': book.summary,
            'comment_count': further_info_queryset['comment_count'],
            'rate_count': further_info_queryset['rate_count'],
            'average_rate': further_info_queryset['average_rate'],
            'count_rate1': further_info_queryset['count_rate1'],
            'count_rate2': further_info_queryset['count_rate2'],
            'count_rate3': further_info_queryset['count_rate3'],
            'count_rate4': further_info_queryset['count_rate4'],
            'count_rate5': further_info_queryset['count_rate5'],
            'reviews': reviews
        }

        return result
