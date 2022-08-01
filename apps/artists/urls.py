from django.urls import path

from . import views

app_name = 'artists'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /artists/5/
    path('<int:artist_id>/', views.detail_canonical, name='detail_id'),
    path('<str:artist_slug>/', views.DetailView.as_view(), name='detail'),
]
