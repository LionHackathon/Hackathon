from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('user/signup', views.signup_view, name='signup'),
    path('user/signin', views.signin_view, name='signin'),
]