from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import ClientSignupForm, ClientLoginForm
from django.contrib import messages

def home(request):
    return render(request, 'clients/home.html')  

def client_signup(request):
    if request.method == 'POST':
        form = ClientSignupForm(request.POST)
        if form.is_valid():
            # Create Django user
            user = User.objects.create_user(
                username=form.cleaned_data['email'],  # email as username
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            
            # Create Client profile linked to user
            client = form.save(commit=False)
            client.user = user
            client.save()

            auth_login(request, user)  # log in user
            return redirect('home')
    else:
        form = ClientSignupForm()

    return render(request, 'clients/client_signup.html', {'form': form})

def signup_success(request):
    return render(request, 'clients/signup_success.html')

# Login view
def client_login(request):
    if request.method == 'POST':
        form = ClientLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = ClientLoginForm()

    return render(request, 'clients/login.html', {'form': form})


# Logout view
def client_logout(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')

def notifications_view(request):
    # You can later fetch notifications from the database
    return render(request, 'clients/notifications.html')
