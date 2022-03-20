from os import access
import jwt, json
from unittest.mock import MagicMock, patch
from unittest      import mock
from datetime      import datetime, timedelta

from django.test   import TestCase, Client

from my_settings   import SECRET_KEY, ALGORITHM
from users.models  import User, Wishlist, WishlistRoom
from rooms.models  import (Room, 
                           RoomAmenity,
                           RoomHouseRule,
                           RoomImage,
                           RoomSchedule,
                           HouseRule,
                           Amenity,
                           AmenityType,
                           Category)


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
        response            = client.get('/users/login/kakao', **headers)  
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
        response            = client.get('/users/login/kakao', **headers)  

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
        response            = client.get('/users/login/kakao')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_ACCESS_TOKEN'})
    
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
        response            = client.get('/users/login/kakao', **headers)  

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'CANNOT_GET_ATTRIBUTE'},)   
        
class WishlistRoomTest(TestCase):
    @classmethod
    def setUp(self):
        user = User.objects.create(
            id            = 1,
            nickname      = "김기현",
            email         = "kimgh6516@naver.com",
            password      = "123",
            profile_image = "http://Helloworld.com",
            gender        = "Male",
            bio           = "Hi",
            birthdate     = "1999-11-02",
            is_superhost  = False,
            kakao_id      = "1",
            github_id     = "1",
        )
        
        room = Room.objects.create(
            id                 = 1,
            name               = "기현네",
            description        = "안녕하세요. 기현네입니다.",
            district           = "서울광역시 종로구",
            neighberhood       = "숭인동",
            price              = 70000,
            address            = "서울시 종로구 숭인동 기현빌딩",
            guests             = 5,
            beds               = 1,
            bedrooms           = 2,
            baths              = 1,
            check_in_time      = "13:00:00",
            check_out_time     = "21:00:00",
            is_instant_booking = False,
            latitute           = 37.5047692,
            longitute          = 127.0062895,
            user_id            = 1,
            category           = Category.objects.create(
            type               = "호텔방"
            ),
        )
        
        room_image = RoomImage.objects.create(
            id        = 1,
            image_url = "http://room_image",
            room_id   = 1
        )
        
        amaenity_type = AmenityType.objects.create(
            id   = 1,
            name = "amenity"
        )
        
        amenity = Amenity.objects.create(
            id               = 1,
            name             = "숟가락",
            amenity_type_id  = 1,
            icon_url         = "http://amenity_icon"
        )
        
        room_amenity = RoomAmenity.objects.create(
            id         = 1,
            room_id    = 1,
            amenity_id = 1
        )
        
        room_schedule = RoomSchedule.objects.create(
            id        = 1,
            check_in  = "2022-03-22",
            check_out = "2022-03-23",
            room_id   = 1
        )
        house_rule = HouseRule.objects.create(
            id       = 1,
            name     = "흡연 불가",
            icon_url = "http://house_rule_icon"
        )
        room_house_rule = RoomHouseRule.objects.create(
            id            = 1,
            room_id       = 1,
            house_rule_id = 1
        )        
        
    def tearDown(self):
        User.objects.all().delete()
        Category.objects.all().delete()
        Room.objects.all().delete()
        AmenityType.objects.all().delete()
        RoomAmenity.objects.all().delete()
        RoomImage.objects.all().delete()
        RoomSchedule.objects.all().delete()
        HouseRule.objects.all().delete()
        RoomHouseRule.objects.all().delete()
        
    def test_get_wishlist_created_success(self):
        client = Client()
        access_token = jwt.encode({
                            'user_id' : 1, 
                            'exp'     : datetime.utcnow() + timedelta(hours=24)
                        }, SECRET_KEY, ALGORITHM)        
        data = {
            'room_id' : 1,
            'name' : 'wishlist_test_name',
            'wishlist_id' : 1
        }
        
        headers  = {'HTTP_Authorization' : access_token}
        url = '/users/wishlist'
        response = client.post(url, json.dumps(data), content_type='application/json', **headers) 
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message' : 'LIKED'})
    
    @patch("users.views.requests")
    def test_get_wishlist_deleted_success(self,mocked_requests):
        client = Client()
        access_token = jwt.encode({
                            'user_id' : 1, 
                            'exp'     : datetime.utcnow() + timedelta(hours=24)
                        }, SECRET_KEY, ALGORITHM)        
        
        class MockedResponse:
            def json(self):
                return {
                 data : {
                    'room_id' : 1,
                    'name' : 'wishlist_test_name',
                    'wishlist_id' : 1,
                    }
                }
        mocked_requests.get = mock.MagicMock(return_value = MockedResponse())
        
        data = {
            'room_id' : 1,
            'name' : 'wishlist_test_name',
            'wishlist_id' : 1,
        }
        headers  = {'HTTP_Authorization' : access_token}
        url = '/users/wishlist'
        response = client.post(url, json.dumps(data), content_type='application/json', **headers) 
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json(), {'result' : 'UNLIKED'})
    
    def test_get_wishlist_invalid_user(self):
        client = Client()
        access_token = jwt.encode({
                            'user_id' : 1, 
                            'exp'     : datetime.utcnow() + timedelta(hours=24)
                        }, SECRET_KEY, ALGORITHM)      
        data = {
            'room_id' : 1,
            'name' : 'wishlist_test_name',
            'wishlist_id' : 1
        }
        
        headers  = {'HTTP_Authorization' : access_token}
        url = '/users/wishlist'
        response = client.post(url, json.dumps(data), content_type='application/json', **headers) 
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'INVALID_USER'})
        
    def test_get_wishlist_room_does_not_exist(self):
        client = Client()
        access_token = jwt.encode({
                            'user_id' : 1, 
                            'exp'     : datetime.utcnow() + timedelta(hours=24)
                        }, SECRET_KEY, ALGORITHM)      
        data = {
            'room_id' : 11111,
            'name' : 'wishlist_test_name',
            'wishlist_id' : 1
        }
        
        headers  = {'HTTP_Authorization' : access_token}
        url = '/users/wishlist'
        response = client.post(url, json.dumps(data), content_type='application/json', **headers) 
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'ROOM_DOES_NOT_EXIST'})    
        
    def test_get_wishlist_keyerror(self):
        client = Client()
        access_token = jwt.encode({
                            'user_id' : 1, 
                            'exp'     : datetime.utcnow() + timedelta(hours=24)
                        }, SECRET_KEY, ALGORITHM)     
        data = {
            'room_id' : 1,
        }
        
        headers  = {'HTTP_Authorization' : access_token}
        url = '/users/wishlist'
        response = client.post(url, json.dumps(data), content_type='application/json', **headers) 
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'KEY_ERROR'})  
        

    def test_get_wishlist_no_authorization_in_header_success(self):
        client = Client()

        wishlist, is_created = Wishlist.objects.get_or_create(
                user_id=1,
                name="wishlist_test_name"
            )
        headers  = {'Content-type' : 'application/json'}
        response = client.post('/users/wishlist', **headers) 
        
        self.assertEqual(response.json(), {'message' : 'NO AUTHORIZATION IN HEADER'})
        self.assertEqual(response.status_code, 401)

    def test_get_wishlist_invalid_token_success(self):
        client = Client()

        wishlist, is_created = Wishlist.objects.get_or_create(
                user_id=1,
                name="wishlist_test_name"
            )
        headers  = {'HTTP_Authorization' : 'fake_access_token'}
        response = client.post('/users/wishlist', **headers) 
        
        self.assertEqual(response.json(), {'message' : 'INVALID_TOKEN'})      
        self.assertEqual(response.status_code, 400)
