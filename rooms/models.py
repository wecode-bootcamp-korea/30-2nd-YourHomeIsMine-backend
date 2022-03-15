from django.db import models

from core.models import TimeStampModel

class RoomType(models.Model):
    type = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'room_types'      

class Room(TimeStampModel):
    name               = models.CharField(max_length=100)
    description        = models.TextField()
    district           = models.CharField(max_length=50)
    neighberhood       = models.CharField(max_length=50)
    price              = models.DecimalField(max_digits=15, decimal_places=2)
    address            = models.CharField(max_length=500)
    guests             = models.PositiveIntegerField()
    beds               = models.PositiveIntegerField()
    bedrooms           = models.PositiveIntegerField()
    baths              = models.PositiveIntegerField()
    check_in_time      = models.TimeField()
    check_out_time     = models.TimeField()
    is_instant_booking = models.BooleanField(default=False)
    latitute           = models.DecimalField(max_digits=15, decimal_places=10)
    longitute          = models.DecimalField(max_digits=15, decimal_places=10)
    user               = models.ForeignKey('users.User', related_name='rooms', on_delete=models.CASCADE)    
    room_type          = models.ForeignKey('RoomType', related_name='rooms', on_delete=models.CASCADE) 
    
    class Meta:
        db_table = 'rooms'   
    
class RoomImage(models.Model):
    image_url = models.CharField(max_length=2000)    
    room      = models.ForeignKey('Room', related_name='room_images', on_delete=models.CASCADE)

    class Meta:
        db_table = 'room_images'  
        
class AmenityType(models.Model):
    name = models.CharField(max_length=50)    
    
    class Meta:
        db_table = 'amenity_types'       

class Amenity(models.Model):
    name         = models.CharField(max_length=100)
    amenity_type = models.ForeignKey('AmenityType', related_name='amenities', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'amenities'      

class RoomAmenity(models.Model):
    room    = models.ForeignKey('Room', related_name='room_amenities', on_delete=models.CASCADE)
    amenity = models.ForeignKey('Amenity', related_name='room_amenities', on_delete=models.CASCADE)

    class Meta:
        db_table = 'room_amenities'      

class HouseRules(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'house_rules'  

class RoomHouseRule(models.Model):
    room = models.ForeignKey('Room', related_name='room_houserules', on_delete=models.CASCADE)

    class Meta:
        db_table = 'room_house_rules'

class RoomSchedule(models.Model):
    check_in  = models.DateField()
    check_out = models.DateField()
    room      = models.ForeignKey('Room', related_name='room_schedules', on_delete=models.CASCADE)
       
    class Meta:
        db_table = 'room_schedules'     