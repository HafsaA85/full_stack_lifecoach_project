from django.shortcuts import render, redirect
from .forms import ClientSignupForm

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
