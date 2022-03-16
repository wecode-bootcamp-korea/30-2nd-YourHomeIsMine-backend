from django.urls import path
from users.views import KakaoSignIn

urlpatterns = [
    path("/login/kakao", KakaoSignIn.as_view()),
]