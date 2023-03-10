from django.urls import path
from user import views as user_view
from django.contrib.auth import views as auth

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
]

