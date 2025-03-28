from django.contrib import admin
from .models import Book

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('title',)
admin.site.register(Book, MemberAdmin)