from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from custom_authentication.models import CustomProfileModel


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Please enter your password again")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class CustomUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    contact_number = forms.CharField(max_length=50)

    class Meta:
      model = CustomProfileModel
      fields = ['first_name', 'last_name', 'email', 'contact_number']
