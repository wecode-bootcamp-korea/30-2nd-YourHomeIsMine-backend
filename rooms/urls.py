from django.urls import path

from rooms.views import RoomDetailView,RoomListView

urlpatterns = [
    path('/<int:room_id>', RoomDetailView.as_view()),
    path("", RoomListView.as_view())
]

