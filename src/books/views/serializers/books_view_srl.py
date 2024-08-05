from rest_framework import serializers


class BooksViewListTRF(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()


class BooksViewRetrieveTRF(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    summary = serializers.CharField()
