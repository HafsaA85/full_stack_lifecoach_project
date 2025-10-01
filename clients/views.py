from django.shortcuts import render, redirect
from .forms import ClientSignupForm
from .models import Client
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
            user = form.save()  # creates User with password
            Client.objects.create(
                user=user,
                phone=form.cleaned_data.get('phone'),
                message=form.cleaned_data.get('message')
            )
            messages.success(request, "Signup successful! You can now log in.")
            return redirect('login')
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

# A simple login form
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


def client_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)        # ✅ correct usage
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect("home")     # or your dashboard
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, "clients/login.html", {"form": form})






