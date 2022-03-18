from django.test import TestCase, Client

from users.models   import User
from rooms.models   import Category, Room
from reviews.models import Review, ReviewImage

class ReviewTest(TestCase):
    def setUp(self):
        test_user = User.objects.create(
            id            = 1,
            nickname      = "은지",
            email         = "monahk93@google.com",
            password      = "qqq",
            profile_image = "1"
        )
        
        test_category = Category.objects.create(
            id   = 1,
            type = "집 전체",
        )
        
        test_room = Room.objects.create(
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
            user               = test_user,
            category           = test_category,
        )
        
        test_review = Review.objects.create(
            id               = 1,
            content          = "내용",
            accuracy         = 5,
            communication    = 5,
            cleanliness      = 5,
            location         = 5,
            check_in         = 5,
            cost_performance = 5,
            user             = test_user,
            room             = test_room,
        )
        
        ReviewImage.objects.create(
            image_url ='1',
            review    = test_review
        )
        
    def tearDown(self):
        User.objects.all().delete()
        Category.objects.all().delete()
        Room.objects.all().delete()
        Review.objects.all().delete()
        
    def test_success_review_view_get_method(self):
        client   = Client()
        response = client.get("/rooms/1/reviews")

        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(response.json(), {
            "message" : "SUCCESS", "result" : {
                "reviews_number"  : 1,
                "star_rating"     : 5.0,
                "accuracy"        : 5.0,
                "communication"   : 5.0,
                "cleanliness"     : 5.0,
                "location"        : 5.0,
                "check_in"        : 5.0,
                "cost_performance": 5.0,
                "reviews"         : [
                    {
                        'profile_image' : '1',
                        'contents'      : "내용",
                        #'date'          : ,
                        'review_image'  : ['1']
                    }
                ]
            }
        })

    def test_review_view_get_room_not_exist(self):
        client   = Client()
        response = client.get("/rooms/2/reviews")

        self.assertEqual(response.status_code, 400)
        
        self.assertEqual(response.json(), {
            "message" : "ROOM_NOT_EXIST"
            }
        )
