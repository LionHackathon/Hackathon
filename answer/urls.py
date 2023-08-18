from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('questions/<int:question_id>/answer/', views.add_answer, name='add_answer'),
    path('questions/<int:question_id>/answers/', views.get_answer_detail_as_json, name='get_answer_detail_as_json'),
]