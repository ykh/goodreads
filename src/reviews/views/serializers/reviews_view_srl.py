from rest_framework import serializers


class ReviewsViewCreateTRF(serializers.Serializer):
    id = serializers.UUIDField()
    user_id = serializers.UUIDField(source='user.id')
    book_id = serializers.UUIDField()
    comment = serializers.CharField()
    rate = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class ReviewsViewUpdateTRF(ReviewsViewCreateTRF):
    pass
