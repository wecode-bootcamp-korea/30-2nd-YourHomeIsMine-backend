from django.urls import path
from users.views import KakaoSignIn, WishlistView

urlpatterns = [
    path("/login/kakao", KakaoSignIn.as_view()),
    path("/wishlist", WishlistView.as_view()),
    
]
