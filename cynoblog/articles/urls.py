from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'articles'

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    # path('', views.article_list, name="list"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('create/', views.article_create, name="create"),
    # path('delete/<str:id>', views.article_delete, name="delete"),
    # path('upload/', views.article_upload, name="upload"),
    # #str:slug should be last because of regex scanning
    # path('<str:slug>/', views.article_details, name='detail'),
]
