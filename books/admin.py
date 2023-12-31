from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'author', 'isbn')
    search_fields = ('title', 'subtitle', 'author', 'isbn')

