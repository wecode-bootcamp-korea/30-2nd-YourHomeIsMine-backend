from django.test import TestCase, Client

from users.models import User
from rooms.models import Amenity, AmenityType, HouseRule, Room, Category, RoomAmenity, RoomHouseRule, RoomImage, RoomSchedule

client = Client()
class RoomDetailViewTest(TestCase):
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
        
        
    def test_get_room_information_success(self):
        result = {
            "name"            : "기현네",
            "description"     : "안녕하세요. 기현네입니다.",
            "district"        : "서울광역시 종로구",
            "neighberhood"    : "숭인동",
            "price"           : 70000.0,
            "address"         : "서울시 종로구 숭인동 기현빌딩",
            "guests"          : 5,
            "beds"            : 1,
            "bedrooms"        : 2,
            "baths"           : 1,
            "latitute"        : 37.5047692,
            "longitute"       : 127.0062895,
            "host"            : "김기현",
            "host_image"      : "http://Helloworld.com",
            "category"        : "호텔방",
            "room_images_url" : ["http://room_image"],
            "check_in"        : ["2022-03-22"],
            "room_amenities"  : [{
                    "amenity_id"       : 1,
                    "amenity_name"     : "숟가락",
                    "amenity_icon_url" : "http://amenity_icon"
            }],
            "check_in_time"  : "13:00:00",
            "check_out_time" : "21:00:00",
            "house_rules" : [{
                    "room_rules"     : "흡연 불가",
                    "rules_icon_url" : "http://house_rule_icon",
                 }]
        }
        
        response = self.client.get('/rooms/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': result})
        
    def test_room_id_does_not_exist(self):
        response = client.get('/rooms/2222', content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'ROOM_DOES_NOT_EXIST')
    
   
        