from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article
from cynoblog.serializers import UserSerializer
from comments.serializers import CommentSerializer

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'desc', 'date', 'author']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        username = author_data.pop('username')
        author = User.objects.get(username=username)
        created_article = Article(author=author, **validated_data)
        created_article.save()

        return created_article

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        username = author_data.pop('username')
        author = User.objects.get(username=username)

        instance.title = validated_data.get('title', instance.title)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.author = author
        instance.save()
        return instance

