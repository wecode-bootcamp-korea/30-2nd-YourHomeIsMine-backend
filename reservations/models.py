from django.db import models

from core.models import TimeStampModel

class Reservation(TimeStampModel):
    reservation_code   = models.CharField(max_length=36, unique=True)
    reservation_status = models.ForeignKey('ReservationStatus', related_name='reservations', on_delete=models.CASCADE)
    check_in           = models.DateField()
    check_out          = models.DateField()
    user               = models.ForeignKey('users.User', related_name='reservations', on_delete=models.CASCADE)
    room               = models.ForeignKey('rooms.Room', related_name='reservations', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'reservations'

class ReservationStatus(models.Model):
    status = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'reservation_statuses'
        
class ReservationItem(models.Model):
    guests        = models.PositiveIntegerField()
    room_schedule = models.ForeignKey('rooms.Room', related_name='reservation_items', on_delete=models.CASCADE)
    reservation   = models.ForeignKey('Reservation', related_name='reservation_items', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'reservation_items'