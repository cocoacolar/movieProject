from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views


urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('get-user/', views.get_user),      # 내가 내 자신을 가져오는 url
    path('get-user-proflie/<int:user_pk>/', views.get_user_profile),      # 누구든지 user 정보를 가져오는 url
]

