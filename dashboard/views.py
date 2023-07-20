from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def dash(request):
    return render(request, 'dashboard.html')


def log_out(request):
    logout(request)
    return render(request, 'logout.html')