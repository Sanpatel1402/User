from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AuthUser
from .forms import MyForm


# Create your views here.


def reg(request):
    return render(request, 'reg.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        birth = request.POST.get('birth')
        password = request.POST.get('pass1')
        pass1 = request.POST.get('pass2')
        print(first_name, last_name, username, email, phone_number, password, pass1)
        if password == pass1:
            my_user = AuthUser.objects.create_user(username, email, first_name, last_name, phone_number, birth, password)
            my_user.save()
            print(my_user)
            return redirect('reg')
        else:
            messages.info(request, 'both password are not same.')
            return redirect('register')
    form = MyForm()
    if form.is_valid():
        messages.success(request, 'your captcha is valid')
    else:
        messages.error(request, 'your captcha is not valid')
    return render(request, 'register.html', {'form': form})
