from rest_framework import serializers


class BookmarksViewBookmarkTRF(serializers.Serializer):
    id = serializers.UUIDField()
    user_id = serializers.UUIDField()
    book_id = serializers.UUIDField()
