from rest_framework import exceptions, serializers


class ReviewsSVCCreateVLD(serializers.Serializer):
    user_id = serializers.UUIDField()
    book_id = serializers.UUIDField()
    comment = serializers.CharField(required=False)
    rate = serializers.IntegerField(required=False)

    def validate(self, data):
        """
        Check that either comment or rate is set.
        """
        if not data.get('comment') and not data.get('rate'):
            raise exceptions.ValidationError("Either 'comment' or 'rate' must be set.")

        return data

    def validate_rate(self, value):
        """
        Check that the rate is between 1 and 5.
        """
        if value is not None and (value < 1 or value > 5):
            raise exceptions.ValidationError('Rate must be between 1 and 5.')

        return value


class ReviewsSVCUpdateVLD(ReviewsSVCCreateVLD):
    pass
