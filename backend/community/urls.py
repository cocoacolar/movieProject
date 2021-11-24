from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list_create),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/delete-update/', views.article_update_delete),
    path('comments/create/', views.comment_create),
    path('comments/<int:comment_pk>/delete/', views.comment_delete),
]