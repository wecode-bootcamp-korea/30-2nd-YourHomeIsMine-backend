from django.urls import path
from users.views import KakaoSignIn, ToggleRoom

urlpatterns = [
    path("/login/kakao", KakaoSignIn.as_view()),
    path("/toggle", ToggleRoom.as_view()),
    
]
