from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from car_models.models import Car, Image


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
    # def __init__(self, *args, **kwargs):
    #     super(UserCreateForm, self).__init__(*args,
    #                                          **kwargs)
    #     for fieldname in ['username', 'password1',
    #                       'password2']:
    #         self.fields[fieldname].help_text = None
    #         self.fields[fieldname].widget.attrs.update(
    #           {'class': 'form-control'})


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'car_model', 'type', 'year', 'engine', 'seats', 'transmission', 'fuel', 'rent_price']


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = []
