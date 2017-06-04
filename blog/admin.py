from django.contrib import admin
from .models import Post, Category, Item

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Item)