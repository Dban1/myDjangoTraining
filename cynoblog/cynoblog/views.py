from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all().order_by('id')
    serializer_class = UserSerializer

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return HttpResponse('about')