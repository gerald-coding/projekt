from django.urls import path
from .views import ReserveView, BookingList

urlpatterns = [
    path('car/<int:id>/reservation/', ReserveView.as_view(), name="reservation"),
    path('booking_list/', BookingList.as_view(), name="BookingListView"),
]
