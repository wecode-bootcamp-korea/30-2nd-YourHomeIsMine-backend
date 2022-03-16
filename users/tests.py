import jwt
from unittest.mock import MagicMock, patch
from unittest      import mock
from datetime      import datetime, timedelta

from django.test   import TestCase, Client

from users.models  import User
from my_settings   import SECRET_KEY, ALGORITHM


class KakaoSignInTest(TestCase):
    def setUp(self):
        User.objects.create(
            id       = 1,
            kakao_id = 2162014437,
            nickname = '김기현',
            email    = 'kimgh6516@naver.com',
            gender   = 'male',
            profile_image = 'http://k.kakaocdn.net/'
        )
        
    def tearDown(self):
        User.objects.all().delete()

    @patch("users.views.requests")
    def test_kakao_signin_create_user_success(self, mocked_requests):
        client = Client()
        
        class MockedResponse:
            def json(self):
                return {
                "id": 2162014437,
                "properties": {
                    "nickname": "김기현",
                },
                "kakao_account": {
                    "profile": {
                    "profile_image_url": "http://k.kakaocdn.net/",
                    "nickname": "김기현",
                    },
                    "email": "kimgh6516@naver.com",
                    "birthday": "1102",
                    "gender": "male"
                }
            }
        
        mocked_requests.get = mock.MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization' : 'fake_access_token'}
        response            = client.get('/users/login/kakao/callback', **headers)  
        user                = User.objects.get(kakao_id=2162014437)
        access_token        = jwt.encode(
                                {'user_id' : user.id, 
                                    'exp': datetime.utcnow() + timedelta(hours=24)
                                    }, SECRET_KEY, ALGORITHM)
        results             = {
                'email'         : "kimgh6516@naver.com",
                'nickname'      : "김기현",
                'profile_image' : "http://k.kakaocdn.net/",
                'gender'        : "male",
                'kakao_id'      : 2162014437
            }  
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
                'message'   : 'SUCCESS',
                'token'     : access_token,
                'results'   : results,
                })                                    
  
    @patch("users.views.requests")
    def test_kakao_signin_create_user_invalid_form_fail(self, mocked_requests):
        client = Client()
        
        class MockedResponse:
            def json(self):
                return {
                "id": 2162014437,
                "properties": {
                    "nickname": "김기현",
                },
                "kakao_account": {
                    "profile": {
                    "nickname": "김기현",
                    },
                    "birthday": "1102",
                    "gender": "male"
                }
            }
        
        mocked_requests.get = mock.MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization' : 'fake_access_token'}
        response            = client.get('/users/login/kakao/callback', **headers)  

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {'message': 'EMAIL_REQUIRED'})   

    @patch("users.views.requests")
    def test_kakao_signin_invalid_token_form_fail(self, mocked_requests):
        client = Client()
        
        class MockedResponse:
            def json(self):
                return {
                "id": 2162014437,
                "properties": {
                    "nickname": "김기현",
                },
                "kakao_account": {
                    "profile": {
                    "profile_image_url": "http://k.kakaocdn.net/",
                    "nickname": "김기현",
                    },
                    "email": "kimgh6516@naver.com",
                    "birthday": "1102",
                    "gender": "male"
                }
            }
        
        mocked_requests.get = mock.MagicMock(return_value = MockedResponse())
        response            = client.get('/users/login/kakao/callback')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID ACCESS TOKEN'})
    
    @patch("users.views.requests")
    def test_kakao_signin_key_error_fail(self, mocked_requests):
        client = Client()
        
        class MockedResponse:
            def json(self):
                return {
                "id": 2162014437,
                "kakao_account": {
                    "profile": {
                    },
                    "email": "kimgh6516@naver.com",
                }
            }
        mocked_requests.get = mock.MagicMock(return_value = MockedResponse())
        headers             = {'HTTP_Authorization' : 'fake_access_token'}
        response            = client.get('/users/login/kakao/callback', **headers)  

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'CANNOT_GET_ATTRIBUTE'},)   