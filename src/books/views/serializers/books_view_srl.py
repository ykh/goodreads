from rest_framework import serializers


class BooksViewListTRF(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    bookmark_count = serializers.IntegerField()


class BooksViewRetrieveTRF(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    summary = serializers.CharField()
