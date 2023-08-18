from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/comments/', views.get_comment_detail_as_json, name='get_comment_detail_as_json'),
]