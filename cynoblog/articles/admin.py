from django.contrib import admin
from . models import Article
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.

admin.site.register(Article, SimpleHistoryAdmin)
