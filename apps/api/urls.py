from django.urls import path, include
from django.conf import settings

from rest_framework import routers

from . import views

# Rest Framework
if settings.DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register(r'artists', views.ArtistViewSet, basename='artists')
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'articles', views.ArticleViewSet, basename='articles')

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]
