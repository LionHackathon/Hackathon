from django.http import JsonResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from user.models import User


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

        # 이곳에서 실제 로그인 로직을 구현하세요
        user = authenticate(request, username=user_id, password=password)
        if user is not None:
            login(request, user)
            response_data = {'message': 'Signin successful'}
        else:
            response_data = {'message': 'Invalid credentials'}
            
        return JsonResponse(response_data)
