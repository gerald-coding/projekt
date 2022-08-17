from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from car_models.models import Car, Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['feedback', 'score']


