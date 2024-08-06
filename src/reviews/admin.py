from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'rate', 'created_at', 'updated_at')
    list_filter = ('rate', 'created_at', 'updated_at', 'user', 'book')
    search_fields = ('user__email', 'book__title', 'comment')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': (
                'id', 'user', 'book', 'rate', 'comment', 'created_at', 'updated_at',
            )
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('user', 'book')

        return self.readonly_fields
