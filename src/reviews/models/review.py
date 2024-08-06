import uuid

from django.contrib.auth import get_user_model
from django.db import models

from books.models import Book


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='reviews')
    comment = models.TextField(blank=True, null=True)
    rate = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'book')
        ordering = ['-created_at']

    def __str__(self):
        return f"Review by {self.user.email} on {self.book.title}"
