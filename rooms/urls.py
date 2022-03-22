from django.urls import path

from rooms.views        import RoomDetailView
from reservations.views import ReservationView

urlpatterns = [
    path('/<int:room_id>', RoomDetailView.as_view()),
    path('/<int:room_id>/reservations/', ReservationView.as_view())
]