from rest_framework import serializers


class BooksViewListTRF(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    bookmark_count = serializers.IntegerField()
    is_bookmarked = serializers.BooleanField(default=False)


class BooksViewRetrieveTRF(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    summary = serializers.CharField()
