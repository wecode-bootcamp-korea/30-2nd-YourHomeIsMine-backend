from django.urls import path, include

urlpatterns = [
    path("users", include('users.urls')),
    path('reviews', include('reviews.urls')),
    path("rooms", include('rooms.urls')),
]

