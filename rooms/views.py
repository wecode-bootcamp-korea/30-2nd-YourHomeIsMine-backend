from datetime          import datetime
from django.http       import JsonResponse
from django.views      import View
from django.db.models  import Q

from rooms.models      import Amenity, Room, RoomAmenity, RoomHouseRule, RoomSchedule
        
class RoomListView(View):
    def get(self, request):
        category        = request.GET.get('category', None)
        check_in        = request.GET.get('check_in', "2022-01-01")
        check_out       = request.GET.get('check_out', "2022-12-31")
        guest           = request.GET.get('guest', 1)
        price_min       = request.GET.get('price_min', 1)
        price_max       = request.GET.get('price_max', 100000000)
        instant_booking = request.GET.get('instant_booking', None)
        bed             = request.GET.get('bed', 1)
        bedroom         = request.GET.get('bedroom', 1)
        bath            = request.GET.get('bath', 1)
        amenity         = request.GET.getlist('amenity',None)
            
        page            = int(request.GET.get('page', 0))
        limit           = int(request.GET.get('limit', 20))
        offset          = (page*limit)
        
        Reservation_period = RoomSchedule.objects.filter(
            check_in__gte  = check_in, 
            check_out__lte = check_out
        )
        available_room_id_list = set([available_room.room_id for available_room in Reservation_period])
            
        q = Q()

        if amenity:
            q &= Q(room_amenities__amenity_id__in=amenity)
        
        if category:
            q &= Q(category_id=category)

        q &= Q(guests__gte=guest)        
        q &= Q(price__rang=[price_min, price_max])            
        q &= Q(beds__gte=bed)        
        q &= Q(bedrooms__gte=bedroom)        
        q &= Q(baths__gte=bath)
        q &= Q(id__in=available_room_id_list)    
        q &= ~Q(is_instant_booking=instant_booking)
        
        rooms = Room.objects.filter(q)[offset:offset+limit]

        results = [{
            'room_name' : room.name,
            'address'   : room.address,
            'schedule'  : 
                datetime.strftime([room_schedule.check_in for room_schedule in room.room_schedules.all()][0], '%m월 %d일')+" ~ "+
                datetime.strftime([room_schedule.check_in for room_schedule in room.room_schedules.all()][-1], '%m월 %d일'),
            'price'     : int(room.price),
            'images'    : [image.image_url for image in room.room_images.all()],
            'latitude'  : float(room.latitute),
            'longitude' : float(room.longitute),
        } for room in rooms]
            
        return JsonResponse({'results' : results}, status=200)


class RoomDetailView(View):
    def get(self, request, room_id):

        if not Room.objects.filter(id=room_id).exists():
            return JsonResponse({'message': 'ROOM_DOES_NOT_EXIST'}, status=404)

        room = Room.objects.select_related('category')\
                           .prefetch_related('room_amenities', 'room_houserules', 'room_images', 'room_schedules').get(id=room_id)

        result = {
            "name"            : room.name,
            "description"     : room.description,
            "district"        : room.district,
            "neighberhood"    : room.neighberhood,
            "price"           : float(room.price),
            "address"         : room.address,
            "guests"          : int(room.guests),
            "beds"            : room.beds,
            "bedrooms"        : room.bedrooms,
            "baths"           : room.baths,
            "latitute"        : float(room.latitute),
            "longitute"       : float(room.longitute),
            "host"            : room.user.nickname,
            "host_image"      : room.user.profile_image,
            "category"        : room.category.type,
            "room_images_url" : [image.image_url for image in room.room_images.all()],
            "check_in"        : [schedule.check_in for schedule in room.room_schedules.all()],
            "room_amenities"  : [{
                    "amenity_id"       : amenity.id,
                    "amenity_name"     : amenity.amenity.name,
                    "amenity_icon_url" : amenity.amenity.icon_url,
                }for amenity in RoomAmenity.objects.filter(room_id=room_id)],
            "check_in_time"  : room.check_in_time,
            "check_out_time" : room.check_out_time,
            "house_rules" : [{
                    "room_rules"     : rules.house_rule.name,
                    "rules_icon_url" : rules.house_rule.icon_url,
                }for rules in RoomHouseRule.objects.filter(room_id=room_id)]    
        }
        return JsonResponse({'message' : result}, status=200)
