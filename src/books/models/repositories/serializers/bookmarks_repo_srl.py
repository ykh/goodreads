from rest_framework import serializers

from books.models import Bookmark


class BookmarksRepoCreateVLD(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'
