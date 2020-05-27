from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comment
from cynoblog.serializers import UserSerializer

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ['body', 'date', 'author']