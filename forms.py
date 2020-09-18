from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
import uuid


class NewUserForm(UserCreationForm):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id=forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name= forms.CharField(required=True)
    last_name= forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    profile_image=forms.FileField(required=True)





    class Meta:
        model = User
        fields = ('profile_image',"username",'first_name','last_name','id','age',"email", "password1", "password2",)

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name= self.cleaned_data['first_name']
        user.last_name= self.cleaned_data['last_name']
        user.age= self.cleaned_data['age']
        user.profile_image= self.cleaned_data['profile_image']
        user.id= self.cleaned_data['id']


        if commit:
            user.save()
        return user






