from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username',]
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }