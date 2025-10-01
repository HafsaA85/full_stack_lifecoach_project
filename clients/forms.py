from django import forms
from .models import Client

class ClientSignupForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']

        # clients/forms.py

from django.contrib.auth.forms import AuthenticationForm

class ClientLoginForm(AuthenticationForm):
    username = forms.CharField(label="Email or Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


