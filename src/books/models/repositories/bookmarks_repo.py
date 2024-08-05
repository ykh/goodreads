from rest_framework import exceptions

from books.models import Book, Bookmark
from books.models.repositories.serializers.bookmarks_repo_srl import \
    BookmarksRepoCreateVLD
from users.models import User


class BookmarksRepo:
    def __init__(self, requester: User):
        self.requester = requester

    def create(self, params) -> Bookmark:
        params_vld = BookmarksRepoCreateVLD(data=params)
        params_vld.is_valid(raise_exception=True)

        bookmark = params_vld.save()

        return bookmark

    def destroy(self, book_id: str):
        try:
            book = Book.objects.get(id=book_id)
            bookmark = Bookmark.objects.get(user=self.requester, book=book)
            bookmark.delete()
        except Book.DoesNotExist:
            raise exceptions.NotFound('Book not found.')
        except Bookmark.DoesNotExist:
            raise exceptions.NotFound('Bookmark not found.')
