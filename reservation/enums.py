from django.db import models


# Choices for Car model fields
class LocationList(models.TextChoices):
    Tirana_international_airport = "Tirana International Airport"
    Tirana_city_center = "Tirana City Center"
    Durres_port = "Durres Sea Port"