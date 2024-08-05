from django.urls import include, path
from rest_framework.routers import DefaultRouter

from books.views.bookmarks_view import BookmarksViewSet
from books.views.books_view import BooksViewSet

router = DefaultRouter()
router.register('books', BooksViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'books/<uuid:book_id>/bookmark/',
        BookmarksViewSet.as_view(
            {
                'post': 'bookmark',
                'delete': 'unbookmark',
            }
        ),
        name='books-bookmark'
    ),
]
