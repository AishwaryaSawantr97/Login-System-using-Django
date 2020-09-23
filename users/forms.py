from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField()
    First_name = forms.CharField()
    Last_name = forms.CharField()
    Age = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username','First_name','Last_name', 'Age','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']