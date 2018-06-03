from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    url(r'^$', views.home, name='home'),
]
