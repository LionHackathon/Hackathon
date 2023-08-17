from django.contrib import admin
from django.urls import path
from . import views
from user.views import KakaoLoginView, KakaoCallbackView
from user.views import KakaoUserInfoView

urlpatterns = [
    path('user/signup/', views.signup_view, name='signup'),
    path('user/signin/', views.signin_view, name='signin'),
    path('oauth/kakao/login/', views.KakaoLoginView.as_view(), name='kakao_login'),
    path('oauth/kakao/login/callback/', views.KakaoCallbackView.as_view(), name='kakao_callback'),
    path('kakao/user_info/', KakaoUserInfoView.as_view(), name='kakao_user_info'),
]