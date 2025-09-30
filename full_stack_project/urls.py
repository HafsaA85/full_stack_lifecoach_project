from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/signup/', permanent=False)),  # root redirects to signup
    path('', include('clients.urls')),  # include your app URLs
]
