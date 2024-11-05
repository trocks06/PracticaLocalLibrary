from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'book')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Language)