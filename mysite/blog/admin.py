from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['created', 'publish', 'updated']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ['title']}
    date_hierarchy = 'publish'
    ordering = ['publish', 'author']
    raw_id_fields = ['author']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'update']
    search_fields = ['name', 'email', 'body']


