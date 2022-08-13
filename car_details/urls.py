from django.urls import path
from . import views

my_app = 'car_details'

urlpatterns = [
    path('car_details/<int:id>/', views.car_details, name="car_details"),
]