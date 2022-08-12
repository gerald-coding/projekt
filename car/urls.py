from django.urls import path
from . import views

urlpatterns = [
    path('car/', views.car, name="car"),
]