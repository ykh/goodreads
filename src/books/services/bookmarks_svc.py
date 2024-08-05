from rest_framework import exceptions

from books.models import Book, Bookmark
from books.models.repositories.bookmarks_repo import BookmarksRepo
from goodreads.utils.singleton import singleton
from goodreads.utils.validators import validate_uuid
from users.models import User


@singleton
class BookmarksService:
    @validate_uuid(
        'book_id',
        exception=exceptions.ValidationError,
        message='Given book id is not valid.',
        is_optional=False,
    )
    def create(self, book_id: str, requester: User) -> Bookmark:
        bookmarks_repo = BookmarksRepo(requester=requester)

        try:
            user = User.objects.get(id=requester.id)
            book = Book.objects.get(id=book_id)
        except User.DoesNotExist:
            raise exceptions.NotFound('User not found.')
        except Book.DoesNotExist:
            raise exceptions.NotFound('Book not found.')

        if Bookmark.objects.filter(user=user, book=book).exists():
            raise exceptions.ValidationError('You have already bookmarked this book.')

        return bookmarks_repo.create(
            params={
                'user': user.id,
                'book': book.id,
            }
        )

    @validate_uuid(
        'book_id',
        exception=exceptions.ValidationError,
        message='Given book_id is not valid.',
    )
    def destroy(self, book_id: str, requester: User) -> None:
        bookmarks_repo = BookmarksRepo(requester=requester)

        return bookmarks_repo.destroy(book_id=book_id)
