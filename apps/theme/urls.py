from django.urls import path, re_path

from . import views

urlpatterns = [
    # path('', views.homepage, name='homepage'),
    path('', views.vuejs, {'resource': ''}, name='homepage'),
    path('vue', views.vuejs, {'resource': ''}, name='vuejs-test'),
    path('<path:resource>', views.vuejs, name='vuejs-app'),
    # re_path(r'^.*/?$', views.vuejs, name='vuejs')
]
