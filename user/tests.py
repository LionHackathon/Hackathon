from django.test import TestCase
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
