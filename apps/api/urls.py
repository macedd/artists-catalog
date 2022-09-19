from django.urls import path, include
from rest_framework import routers

from . import views

# Rest Framework
router = routers.DefaultRouter()
router.register(r'artists', views.ArtistViewSet)
router.register(r'categories', views.CategoryViewSet)

app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]
