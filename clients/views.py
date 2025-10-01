from django.shortcuts import render, redirect
from .forms import ClientSignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import ClientLoginForm

def client_signup(request):
    if request.method == 'POST':
        form = ClientSignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to your existing success page
            return redirect('signup_success')
    else:
        form = ClientSignupForm()
    return render(request, 'clients/client_signup.html', {'form': form})

def signup_success(request):
    return render(request, 'clients/signup_success.html')


from django.shortcuts import render


@login_required
def notifications_view(request):
    notifications = request.user.notification_set.all().order_by('-timestamp')
    return render(request, 'clients/notifications.html', {'notifications': notifications})

def client_login(request):
    if request.method == "POST":
        form = ClientLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # redirect to home page
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = ClientLoginForm()
    return render(request, 'clients/client_login.html', {'form': form})






