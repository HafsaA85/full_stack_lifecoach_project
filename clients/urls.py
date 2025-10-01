from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # <-- Home page
    path('signup/', views.client_signup, name='client_signup'),
    path('signup/success/', views.signup_success, name='signup_success'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('login/', views.client_login, name='client_login'),
]
