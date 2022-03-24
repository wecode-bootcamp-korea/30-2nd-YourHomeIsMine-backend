import json, uuid

from datetime         import datetime, timedelta
from django.db.models import Q
from django.db        import transaction
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
            check_in  = datetime.strptime(data['check_in'],'%Y-%m-%d')
            check_out = datetime.strptime(data['check_out'],'%Y-%m-%d')
            guests    = data['guests']
            
            if check_in < datetime.today() :
                return JsonResponse({'message' : 'NO_WAY_TO_BOOK_BEFORE_TODAY'}, status=400)
            
            if check_out < check_in :
                return JsonResponse({'message' : 'INVALID_BOOKING_DATE'}, status=400)
            
            q = Q() 
            q |= Q(check_in__range  = [check_in,check_out-timedelta(days=1)])
            q |= Q(check_out__range = [check_in+timedelta(days=1),check_out])
            
            if Reservation.objects.filter(q, room_id=room_id, user=request.user).exists():
                return JsonResponse({'message' : 'DOUBLE_BOOKED_FOR_THE_DAY'}, status=400)

            room = Room.objects.get(id=room_id)
            
            if data['guests'] > room.guests:
                return JsonResponse({'message' : 'EXCESSIVE_NUMBER_OF_PEOPLE'}, status=400)

            with transaction.atomic():
                
                reservation = Reservation.objects.create(
                            reservation_code      = str(uuid.uuid4()),
                            reservation_status_id = 1,
                            check_in              = check_in,
                            check_out             = check_out,
                            user                  = request.user,
                            room                  = room
                        )
                
                for i in range(int((check_out-check_in).days)):
                    date = datetime.date(check_in + timedelta(days=i))
                    
                    if date not in room.room_schedules.values_list('check_in', flat=True):
                        raise RuntimeError
                        
                    ReservationItem.objects.create(
                            guests        = guests,
                            room_schedule = room.room_schedules.get(check_in=date),
                            reservation   = reservation    
                        )

                return JsonResponse({'message' : 'SUCCESS'}, status=201)
        
        except RoomSchedule.DoesNotExist:
            return JsonResponse({'message' : 'RESERVATION_NOT_AVAILABLE'}, status=400)
        
        except RuntimeError:
            return JsonResponse({'message' : 'INAVAILABLE_DATE'}, status=400)
        
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)