import json, jwt

from django.test import TestCase, Client

from users.models   import User
from rooms.models   import Room, Category
from reviews.models import Review, ReviewImage
from my_settings    import ALGORITHM, SECRET_KEY

class ReviewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            id            = 1,
            nickname      = "은지",
            email         = "monahk93@google.com",
            password      = "qqq",
            profile_image = "www.test.1"
        )
        cls.token   = jwt.encode({'user_id' :User.objects.get(id=1).id}, SECRET_KEY, algorithm = ALGORITHM)
        cls.header  = {'HTTP_Authorization' : cls.token}
        cls.payload = jwt.decode(cls.token, SECRET_KEY, algorithms = ALGORITHM)
        
        test_category = Category.objects.create(
            id   = 1,
            type = "집 전체",
        )
        
        cls.test_room = Room.objects.create(
            id                 = 1,
            name               = "방1",
            description        = "쓸쓸한방",
            district           = "강남구",
            neighberhood       = "역삼2동",
            price              = 10000.00,
            address            = "선릉로1길",
            guests             = 5,
            beds               = 5,
            bedrooms           = 5,
            baths              = 5,
            check_in_time      = "13:00:00",
            check_out_time     = "14:00:00",
            is_instant_booking = True,
            latitute           = 34.6750,
            longitute          = 102.3043,
            user               = cls.user,
            category           = test_category,
        )
        
    def tearDown(self):
            User.objects.all().delete()
            Category.objects.all().delete()
            Room.objects.all().delete()
            Review.objects.all().delete()
            ReviewImage.objects.all().delete()

    def test_success_review_view_post_method(self):
        client   = Client()
        review   = {
            id                 : 1,
            "content"          : "내용",
            "accuracy"         : 5,
            "communication"    : 5,
            "cleanliness"      : 5,
            "location"         : 5,
            "check_in"         : 5,
            "cost_performance" : 5,
            "user"             : self.user,
            "room"             : self.test_room,
        }
        response = client.post("http://127.0.0.1:8000/rooms/1/reviews", review, **self.header)
        
        self.assertEqual(response.status_code, 201)
        
        self.assertEqual(response.json(), 
            {
                'message' : 'SUCCESS'
            }
        )

    def test_KeyError_review_view_post_method(self):
        client   = Client()
        review   = {
            id                 : 1,
            #"content"          : "내용",
            "accuracy"         : 5,
            "communication"    : 5,
            "cleanliness"      : 5,
            "location"         : 5,
            "check_in"         : 5,
            "cost_performance" : 5,
            "user"             : self.user,
            "room"             : self.test_room,
        }
        response = client.post("http://127.0.0.1:8000/rooms/1/reviews", review, **self.header)
        
        self.assertEqual(response.json(), 
            {
                'message' : 'KEY_ERROR'
            }
        )              
    