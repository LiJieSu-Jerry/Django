from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('article_view',views.ArticleView,name='article_view'),
]
