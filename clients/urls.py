from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.client_signup, name='client_signup'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('signup/success/', views.signup_success, name='signup_success'),
    path('login/', views.client_login, name='login'),
    path('logout/', views.client_logout, name='logout'),
    path('', views.home, name='home'),
]

