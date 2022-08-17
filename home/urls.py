from django.urls import path
from .views import home, about, contact, SendMail

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('contact/send-mail/', SendMail, name="sendmail"),
]