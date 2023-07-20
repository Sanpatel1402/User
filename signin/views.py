from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import MyForm


# Create your views here.


def log(request):
    return render(request, 'log.html')


def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('pass')
    form = MyForm(request.POST)

    if request.method == "POST":
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            if form.is_valid():
                login(request, user)
                return redirect('log')
            else:
                messages.error(request, 'your captcha is not valid')
                return redirect('login')
        else:
            messages.info(request, 'please enter your correct username or password.')
    return render(request, 'login.html', {'form': form})
