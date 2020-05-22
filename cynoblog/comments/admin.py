from django.contrib import admin
from . models import Comment
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

class CommentAdmin(SimpleHistoryAdmin):
    list_display = ('body', 'date', 'author')
    list_filter = ('date', 'author', 'article')
    # search_fields = ('article', 'author', 'body', 'date')
    search_fields = ['body',]
    actions = ['']

admin.site.register(Comment, CommentAdmin)
