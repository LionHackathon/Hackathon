from django.http import JsonResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import json
import logging
from user.models import User
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
import requests

from django.conf import settings

logger = logging.getLogger(__name__)


@csrf_exempt
def signup_view(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            user_id = data.get('userId')
            password = data.get('password')
            role = data.get('role')

            user = User.objects.create_user(username=user_id, password=password, role=role)
            user.save()

            response_data = {'message': 'Signup successful'}
            return JsonResponse(response_data)
    except Exception as e:
        # 예외가 발생하면 로그에 기록
        logger.error(f"Signup error: {e}")
        return HttpResponseServerError("Internal server error")


@csrf_exempt
def signin_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('userId')
        password = data.get('password')

        user = authenticate(request, username=user_id, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Signin successful'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)

      
class KakaoLoginView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        # 카카오 로그인 페이지 URI로 리다이렉트
        client_id = settings.KAKAO_CONFIG['KAKAO_REST_API_KEY']
        redirect_uri = settings.KAKAO_CONFIG['KAKAO_REDIRECT_URI']
        kakao_login_uri = settings.KAKAO_CONFIG['kakao_login_uri']
        uri = f"{kakao_login_uri}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        return redirect(uri)
    

class KakaoCallbackView(APIView):
    permission_classes = (AllowAny,)

    def get_kakao_user_info(self, access_token):
        kakao_profile_uri = settings.KAKAO_CONFIG['kakao_profile_uri']
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        response = requests.get(kakao_profile_uri, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get(self, request):
        # 코드로 액세스 토큰 받기
        code = request.GET.get('code')
        kakao_token_uri = settings.KAKAO_CONFIG['kakao_token_uri']
        request_data = {
            'grant_type': 'authorization_code',
            'client_id': settings.KAKAO_CONFIG['KAKAO_REST_API_KEY'],
            'redirect_uri': settings.KAKAO_CONFIG['KAKAO_REDIRECT_URI'],
            'client_secret': settings.KAKAO_CONFIG['KAKAO_CLIENT_SECRET_KEY'],
            'code': code,
        }
        token_res = requests.post(kakao_token_uri, data=request_data)
        token_json = token_res.json()
        access_token = token_json.get('access_token')

        # 액세스 토큰으로 사용자 정보 받기
        user_info = self.get_kakao_user_info(access_token)
        if not user_info:
            return Response({"message": "Failed to get user info from Kakao."}, status=400)

        # 사용자 정보로 로그인 또는 회원가입 처리
        user_email = user_info['kakao_account'].get('email')
        try:
            user = User.objects.get(email=user_email)
            login(request, user)
        except User.DoesNotExist:
            user = User.objects.create_user(username=user_email, email=user_email)
            user.save()
            login(request, user)

        return Response({"message": "Success", "user_info": user_info})
