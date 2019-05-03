from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages

from .forms import SignUpForm

def s1(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://doctorcityvn.pythonanywhere.com')
    else:
        form = UserCreationForm()
        messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'registration/s1.html', {'form': form})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.userp.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('http://doctorcityvn.pythonanywhere.com')
    else:
        form = SignUpForm()
        messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'registration/signup.html', {'form': form})

def s2(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://doctorcityvn.pythonanywhere.com')
    else:
        form = SignUpForm()
        messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'registration/s2.html', {'form': form})

def my_view(request):
     user = request.POST.get('username')
     password = request.POST.get('password')
     user = authenticate(username=user, password=password)
     if user is not None:
         login(request, user)
         return redirect("http://doctorcityvn.pythonanywhere.com/menu/")
     else:
         messages.add_message(request, messages.INFO, 'Hello world.')
         return render(request, 'registration/login1.html')
def logout_view(request):
    logout(request)
    # Redirect to a success page.