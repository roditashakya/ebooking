from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models

class SearchForm(forms.ModelForm):
    class Meta:
        fields = ["from_address", "to_address", "departure_date", "return_date", "passengers"]
        model = models.Search

class SigninForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(max_length=250, widget=forms.PasswordInput)

class SignupForm(UserCreationForm):

    class Meta:
       model = User
       fields = ["username", "email", "password1", "password2"]

# class PasswordResetForm(forms.Form):
#     email = forms.EmailField(max_length=250)

# class ScheduleForm(forms.ModelForm):
#     class Meta:
#         model = Schedule
#         fields = '__all__'