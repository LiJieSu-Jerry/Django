from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('resume',views.Resume,name='resume'),
    path('login',views.Login,name='login'),
    path('user_check',views.User_check, name='user_check'),
    path('response_receive_post',views.Response_receive_post, name='response_receive_post'),
    path('response_create',views.Response_create,name='response_create')
]
