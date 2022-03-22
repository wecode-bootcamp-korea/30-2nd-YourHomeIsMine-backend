import json, uuid

from datetime         import datetime
from django.db.models import Q
from django.http      import JsonResponse
from django.views     import View

from core.utils          import login_decorator
from rooms.models        import Room, RoomSchedule
from reservations.models import Reservation, ReservationItem

class ReservationView(View):
    @login_decorator
    def post(self, request, room_id):
        try:
            data      = json.loads(request.body)
            check_in  = datetime(data['check_in'])
            check_out = datetime(data['check_out'])
            guests    = data['guest']
            
            if check_in < datetime.now() :
                return JsonResponse({'message' : 'NO_WAY_TO_BOOK_BEFORE_TODAY'}, status=403)
            
            if check_out < check_in :
                return JsonResponse({'message' : 'INVALID_BOOKING_DATE'}, status=403)
            
            q = Q(room_id=room_id, user=request.user)                                                                                                                                              

            if Reservation.objects.filter(q & Q(check_in__range=[check_in,check_out]) | q & Q(check_out__range=[check_in,check_out])):
                return JsonResponse({'message' : 'DOUBLE_BOOKED_FOR_THE_DAY'}, status=403)

            room = Room.objects.get(room_id)
            
            if int(data['guests'])<= room.guests:
                return JsonResponse({'message' : 'EXCESSIVE_NUMBER_OF_PEOPLE'}, status=403)

            reservation = Reservation.objects.create(
                reservation_code = str(uuid.uuid4),
                check_in         = check_in,
                check_out        = check_out,
                user             = request.user,
                room             = room
            )
            for i in range((datetime(check_out)-datetime(check_in)).days):
                ReservationItem.objects.create(
                    guests        = guests,
                    room_schedule = room.room_schedules.get(check_in=check_in+datetime.day(i)),
                    reservation   = reservation    
                )
            
        except RoomSchedule.DoesNotExist:
            return JsonResponse({'message' : 'RESERVATION_NOT_AVAILABLE'}, status=400)
        