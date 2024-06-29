from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('data/', views.data),
    path('test/', views.test),
]