from django.urls import include, path
from rest_framework.routers import DefaultRouter

from books.views.books_view import BooksViewSet

router = DefaultRouter()
router.register('books', BooksViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls))
]
