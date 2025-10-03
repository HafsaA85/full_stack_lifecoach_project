from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'created_at')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')

    def username(self, obj):
        return obj.user.username

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email
