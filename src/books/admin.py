from django.contrib import admin

from books.models.book import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'isbn', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')
    fields = (
        'title',
        'author',
        'isbn',
        'summary',
        'created_at',
        'updated_at',
    )


admin.site.register(Book, BookAdmin)
