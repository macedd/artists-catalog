from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    # ex: /news/5/
    path('<int:article_id>/', views.detail_canonical, name='detail_id'),
    path('<str:article_slug>/', views.detail_redirect, name='detail'),
]
