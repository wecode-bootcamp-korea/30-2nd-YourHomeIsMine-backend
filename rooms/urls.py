from django.urls import path

from rooms.views   import RoomDetailView
from reviews.views import ReviewView 

urlpatterns = [
    path('/<int:room_id>', RoomDetailView.as_view()),
    path('/<int:room_id>/reviews', ReviewView.as_view()),
    path('/<int:room_id>/reviews/<int:review_id>', ReviewView.as_view())
]