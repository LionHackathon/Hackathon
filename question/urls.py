from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('questions/', views.questions_as_json, name='get-question'),
    path('questions/<int:question_id>/', views.get_question_detail_as_json, name='get_question_detail_as_json'),
    path('', TemplateView.as_view(template_name='question.html'), name='home'),
    path('questions/question_write/', views.question_write, name='question_write')
]