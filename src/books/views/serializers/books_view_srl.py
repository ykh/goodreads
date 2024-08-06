from rest_framework import serializers


class BooksViewListTRF(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    bookmark_count = serializers.IntegerField()
    is_bookmarked = serializers.BooleanField(default=False)


class BooksViewReviewSerializer(serializers.Serializer):
    comment = serializers.CharField(required=False, allow_blank=True)
    rate = serializers.IntegerField(required=False, allow_null=True)


class BooksViewRetrieveTRF(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField()
    comment_count = serializers.IntegerField()
    rate_count = serializers.IntegerField()
    average_rate = serializers.FloatField()
    count_rate1 = serializers.IntegerField()
    count_rate2 = serializers.IntegerField()
    count_rate3 = serializers.IntegerField()
    count_rate4 = serializers.IntegerField()
    count_rate5 = serializers.IntegerField()
    reviews = BooksViewReviewSerializer(many=True)
