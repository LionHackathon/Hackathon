from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.post_as_json, name='get-post'),
    path('post/<int:post_id>/', views.get_post_detail_as_json, name='get_post_detail_as_json'),
]