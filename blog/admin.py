from django.contrib import admin
from .models import Post, Category, Comment


# Register your models here.

admin.site.register(Post)
admin.site.register(Category)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')
admin.site.register(Comment, CommentAdmin)
