from django.urls import path
from . import views

urlpatterns = [
    path('car_details/', views.car_details),
]