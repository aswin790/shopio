from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class loginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.PasswordInput()
class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

