from rest_framework import serializers

from reviews.models import Review


class ReviewsRepoCreateVLD(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewsRepoUpdateVLD(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('user', 'book')
