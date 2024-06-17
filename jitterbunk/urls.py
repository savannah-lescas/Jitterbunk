from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user/<str:username>/', views.user_detail, name='user_detail'),
    path('bunker/', views.submit_bunk, name="submit_bunk"),
]

