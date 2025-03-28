from django.contrib import admin
from .models import *


admin.site.register(Tags)
admin.site.register(Categories)

@admin.register(BookDetail)
class BookDetail(admin.ModelAdmin):
    list_display = ['title','author','category','price']

@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ['author_name']

# Register your models here.