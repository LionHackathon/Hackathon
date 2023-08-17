from django.test import TestCase, Client
from django.urls import reverse
from user.models import User
import json

class SignupAPITest(TestCase):
    def test_signup_view(self):
        url = reverse('signup')  # 'signup'은 회원 가입 뷰의 URL 이름입니다.
        data = {
            'userId': 'testuser',
            'password': 'testpassword',
            'role': 'user'
        }

        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Signup successful')
        self.assertTrue(User.objects.filter(username='testuser').exists())


class SigninAPITest(TestCase):
    def setUp(self):
        # 테스트 데이터 설정
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword', role='user')
        self.signin_url = reverse('signin_view')  # 'signin_view'는 urls.py에서 정의한 signin_view의 이름입니다.

    def test_signin_successful(self):
        # 로그인 성공 테스트
        response = self.client.post(self.signin_url, json.dumps({'userId': 'testuser', 'password': 'testpassword'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Signin successful'})

    def test_signin_invalid_credentials(self):
        # 로그인 실패 테스트
        response = self.client.post(self.signin_url, json.dumps({'userId': 'testuser', 'password': 'testpassword123'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)  # 예상되는 실패 응답 코드는 API 디자인에 따라 다를 수 있습니다.
        self.assertEqual(response.json(), {'message': 'Invalid credentials'})