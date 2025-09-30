from django import forms
from .models import Client

class ClientSignupForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']

