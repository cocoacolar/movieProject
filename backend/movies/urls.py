from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list),
    path('genres/', views.genre_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('comments/create/', views.comment_create),
]