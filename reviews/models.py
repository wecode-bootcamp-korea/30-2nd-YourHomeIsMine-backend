from django.db              import models
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import TimeStampModel

class Review(TimeStampModel):
    content          = models.TextField()
    accuracy         = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    communication    = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    cleanliness      = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    location         = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    check_in         = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    cost_performance = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user             = models.ForeignKey('users.User', related_name='reviews', on_delete=models.CASCADE)
    room             = models.ForeignKey('rooms.Room', related_name='reviews', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'reviews'

class ReviewImage(models.Model):
    image_url = models.CharField(max_length=2000)
    review    = models.ForeignKey('Review',related_name='review_images', on_delete=models.CASCADE)     
    
    class Meta:
        db_table = 'review_images'