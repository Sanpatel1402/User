from django.shortcuts import render

# Create your views here.


def user(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')