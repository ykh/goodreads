import uuid

from django.contrib.auth import get_user_model
from django.db import models

from books.models.book import Book


class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='bookmarks',
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='bookmarks')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} bookmarked {self.book.title}"
