from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
    path('edit/<str:id>', views.comment_edit, name="edit"),
    path('delete/<str:id>', views.comment_delete, name="delete"),
]