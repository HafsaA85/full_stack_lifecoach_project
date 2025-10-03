# clients/models.py
from django.db import models


class Client(models.Model):
    # Basic client info
    full_name = models.CharField(max_length=100, blank=True, null=True)     
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Notification(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    message = models.TextField()
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.client.full_name}: {self.message}"
