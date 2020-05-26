from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article
from cynoblog.serializers import UserSerializer

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Article
        fields = ['title', 'desc', 'date', 'author']

