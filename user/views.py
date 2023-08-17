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
        '''
        kakao code 요청
        '''
        client_id = settings.KAKAO_CONFIG['KAKAO_REST_API_KEY']
        redirect_uri = settings.KAKAO_CONFIG['KAKAO_REDIRECT_URI']
        kakao_login_uri = settings.KAKAO_CONFIG['kakao_login_uri']

        uri = f"{kakao_login_uri}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        
        res = redirect(uri)
        return res



class KakaoCallbackView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        '''
        kakao access_token 요청 및 user_info 요청
        '''
        data = request.query_params.copy()

        kakao_token_uri = settings.kakao_token_uri
        kakao_profile_uri = settings.kakao_profile_uri

        # access_token 발급 요청
        code = data.get('code')
        if not code:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        request_data = {
            'grant_type': 'authorization_code',
            'client_id': settings.KAKAO_CONFIG['KAKAO_REST_API_KEY'],
            'redirect_uri': settings.KAKAO_CONFIG['KAKAO_REDIRECT_URI'],
            'client_secret': settings.KAKAO_CONFIG['KAKAO_CLIENT_SECRET_KEY'],
            'code': code,
        }
        token_headers = {
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
        token_res = requests.post(kakao_token_uri, data=request_data, headers=token_headers)

        token_json = token_res.json()
        access_token = token_json.get('access_token')

        if not access_token:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        access_token = f"Bearer {access_token}"  # 'Bearer ' 마지막 띄어쓰기 필수

        # kakao 회원정보 요청
        auth_headers = {
            "Authorization": access_token,
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        user_info_res = requests.get(kakao_profile_uri, headers=auth_headers)
        user_info_json = user_info_res.json()

        social_type = 'kakao'
        social_id = f"{social_type}_{user_info_json.get('id')}"

        kakao_account = user_info_json.get('kakao_account')
        if not kakao_account:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user_email = kakao_account.get('email')

        # 시스템 내 사용자 확인 및 로그인/등록 처리
        try:
            user = User.objects.get(email=user_email)
            login(request, user)  # 해당 사용자로 로그인 처리
        except User.DoesNotExist:
            # 새로운 사용자 생성
            user = User.objects.create_user(username=user_email, email=user_email)
            user.save()
            login(request, user)  # 새로 생성한 사용자로 로그인 처리

        # 테스트 값 확인용
        res = {
            'social_type': social_type,
            'social_id': social_id,
            'user_email': user_email,
        }
        response = Response(status=status.HTTP_200_OK)
        response.data = res
        return response