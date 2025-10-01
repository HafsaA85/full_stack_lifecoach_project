# clients/models.py
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class Client(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField(blank=True)
    password = models.CharField(max_length=128, default="")


    def __str__(self):
        return self.username  # or self.email if you want to use email as login



class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user}: {self.message}"

