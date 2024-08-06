from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from books.services.bookmarks_svc import BookmarksService
from books.views.serializers.bookmarks_view_srl import BookmarksViewBookmarkTRF


class BookmarksViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bookmarks_svc = BookmarksService()

    @action(detail=True, methods=['post'])
    def bookmark(self, request, book_id):
        bookmark = self.bookmarks_svc.create(
            book_id=book_id,
            requester=request.user,
        )

        return Response(
            data=BookmarksViewBookmarkTRF(
                instance=bookmark,
            ).data,
            status=status.HTTP_201_CREATED,
        )

    @action(detail=True, methods=['delete'])
    def unbookmark(self, request, book_id):
        self.bookmarks_svc.destroy(
            book_id=book_id,
            requester=request.user,
        )

        return Response(status=status.HTTP_200_OK)
