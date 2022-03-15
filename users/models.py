from django.db import models

from core.models import TimeStampModel

class User(TimeStampModel):
    nickname      = models.CharField(max_length=50)
    email         = models.EmailField(max_length=100, unique=True)
    password      = models.CharField(max_length=200)
    profile_image = models.CharField(max_length=2000)
    gender        = models.CharField(max_length=50, null=True)
    bio           = models.TextField(null=True)
    birthdate     = models.DateField(null=True)
    is_superhost  = models.BooleanField(default=False)
    kakao_id      = models.CharField(max_length=200, null=True)
    github_id     = models.CharField(max_length=200, null=True)
    
    class Meta:
        db_table = 'users'
    
class Wishlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('User', related_name='wishlists', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'wishlists'
            
class WishlistRoom(models.Model):
    room     = models.ForeignKey('rooms.Room', related_name='wishlist_rooms', on_delete=models.CASCADE)
    wishlist = models.ForeignKey('Wishlist', related_name='wishlist_rooms', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'wishlist_rooms'