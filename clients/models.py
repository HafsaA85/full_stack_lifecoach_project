from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Notification(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        message = models.TextField()
        read = models.BooleanField(default=False)
        timestamp = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
            return f"Notification for {self.user.username}: {self.message}"
