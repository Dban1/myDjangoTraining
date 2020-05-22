from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('delete/<str:id>', views.article_delete, name="delete"),
    path('upload/', views.article_upload, name="upload"),
    #str:slug should be last because of regex scanning
    path('<str:slug>/', views.article_details, name='detail'),
]