# clients/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Client, Notification
from django.contrib.auth.models import User

@receiver(post_save, sender=Client)
def client_signup_notification(sender, instance, created, **kwargs):
    if created:
        # --- Email to Admin ---
        send_mail(
            subject='New Client Signup',
            message=f'Client {instance.full_name} has signed up with email {instance.email}.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['admin@example.com'],  # replace with actual admin email(s)
        )

        # --- In-App Notification ---
        # Assuming admin user exists with username 'admin'
        try:
            admin_user = User.objects.get(username='admin')
            Notification.objects.create(
                user=admin_user,
                message=f'New client signed up: {instance.full_name} ({instance.email})'
            )
        except User.DoesNotExist:
            print("Admin user not found. Notification not sent.")
