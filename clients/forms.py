from django import forms
from django.contrib.auth.models import User
from .models import Client
from django.contrib.auth.forms import AuthenticationForm

class ClientSignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ['phone', 'message']  # only Client fields


# Login form
class ClientLoginForm(AuthenticationForm):
    username = forms.CharField(label="Email or Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
