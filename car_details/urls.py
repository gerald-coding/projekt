from django.urls import path
from . import views

urlpatterns = [
    path('car_details/<int:id>/', views.car_details, name="car_details"),
    path('car_details/review/<int:id>/', views.review, name="review"),
    path('car_details/update_review/<int:id>/', views.update_review, name="update_review"),
    path('car_details/delete_review/<int:id>/', views.delete_review, name="delete_review"),
]