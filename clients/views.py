from django.shortcuts import render, redirect
from .forms import ClientSignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import ClientLoginForm


def home(request):
    # Render a home page template (not the signup form)
    return render(request, 'clients/home.html')

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
    """
    Handles client login.
    - Displays login form on GET request.
    - Authenticates and logs in the user on POST request.
    - Redirects to home page on successful login.
    - Shows error message on invalid credentials.
    """
    if request.user.is_authenticated:
        # Redirect already logged-in users to home
        return redirect('home')

    form = ClientLoginForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'clients/client_login.html', {'form': form})







