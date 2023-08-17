from django.contrib import admin
from django.urls import path
from . import views
from user.views import KakaoLoginView, KakaoCallbackView

urlpatterns = [
    path('user/signup/', views.signup_view, name='signup'),
    path('user/signin/', views.signin_view, name='signin'),
    path('kakao/login/', views.KakaoLoginView.as_view(), name='kakao_login'),
    path('kakao/login/callback/', views.KakaoCallbackView.as_view(), name='kakao_callback'),
]