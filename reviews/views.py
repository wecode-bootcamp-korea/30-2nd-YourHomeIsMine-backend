import boto3, uuid

from django.http  import JsonResponse
from django.views import View

from rooms.models import Room
from .models      import Review, ReviewImage
from core.utils   import login_decorator
from my_settings  import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_URL

class ReviewView(View): 
    @login_decorator  
    def post(self, request, room_id):
        try:
            review = Review.objects.create(
                content          = request.POST['content'],
                accuracy         = request.POST['accuracy'],
                communication    = request.POST['communication'],
                cleanliness      = request.POST['cleanliness'],
                location         = request.POST['location'],
                check_in         = request.POST['check_in'],
                cost_performance = request.POST['cost_performance'],
                user             = request.user,
                room             = Room.objects.get(id=room_id)    
            )

            review_images = request.FILES.getlist('review_images')
            
            if review_images:
                s3_client = boto3.client(
                    's3',
                    aws_access_key_id     = AWS_ACCESS_KEY_ID,
                    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
                )
                   
                for i in range(len(review_images)):
                    file      = review_images[i]
                    file_name = str(uuid.uuid4())
                    s3_client.upload_fileobj(
                        file,
                        's3-yhim',
                        file_name,
                        ExtraArgs = {'ContentType' : file.content_type}
                    )
                    ReviewImage.objects.create(
                        image_url = file_name,
                        review    = review
                    )
                    
            return JsonResponse({'message':'SUCCESS'}, status=201)
        
        except KeyError: 
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        