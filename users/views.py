import requests, jwt, datetime

from django.views           import View
from django.http            import JsonResponse
from django.shortcuts       import redirect

from .models     import User
from my_settings import CLIENT_ID, SECRET_KEY, ALGORITHM


class KakaoLogin(View):
    def get(self, request):
        client_id      = CLIENT_ID
        redirect_uri   = "http://127.0.0.1:8000/users/login/kakao/callback"
        kakao_auth_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
        return redirect(
            f"{kakao_auth_api}&client_id={client_id}&redirect_uri={redirect_uri}"
        )


class KakaoCallback(View):
    def get(self, request):
        
        try:
            code            = request.GET.get("code")
            client_id       = CLIENT_ID
            redirect_uri    = "http://127.0.0.1:8000/users/login/kakao/callback"
            kakao_token_api = "https://kauth.kakao.com/oauth/token"
   
            data = {
                'grant_type'      : 'authorization_code',
                'client_id'       : client_id,
                'redirection_uri' : redirect_uri,
                'code'            : code,   
            }
            token_response = requests.post(kakao_token_api, data=data)
            
            kakao_token = token_response.json().get("access_token")
            
            profile_request = requests.get(
                "https://kapi.kakao.com/v2/user/me",
                headers = {"Authorization": f"Bearer {kakao_token}"},
                timeout = 2
            )      
                  
            profile_json  = profile_request.json()
            email         = profile_json.get("kakao_account").get("email", None)
            nickname      = profile_json.get("properties").get("nickname")
            profile_image = profile_json.get("kakao_account").get("profile").get("profile_image_url")
            gender        = profile_json.get("kakao_account").get("gender", None)
            kakao_id      = profile_json.get("id")
            
            
            if email is None:
                return JsonResponse({'message': 'EMAIL_REQUIRED'}, status = 405)
        
        
            user, flag = User.objects.get_or_create(
                kakao_id      = kakao_id,
                defaults={
                'email'         : email,
                'nickname'      : nickname,
                'profile_image' : profile_image,
                'gender'        : gender
                }
            )
            user.save()
                
            access_token = jwt.encode(
                {'user_id' : user.id, 
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
                    }, SECRET_KEY, ALGORITHM)

            result = {
                'email'         : email,
                'nickname'      : nickname,
                'profile_image' : profile_image,
                'gender'        : gender,
                'kakao_id'      : kakao_id
                    }               
    
            return JsonResponse(
                {
                    'message'   : 'SUCCESS',
                    'token'     : access_token,
                    'user_info' : result
                }, status = 200)                                    

        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
            
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message' : 'EXPIRED_TOKEN'}, status = 400)  