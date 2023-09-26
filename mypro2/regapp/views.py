from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['p1']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['f_name']
        lastname = request.POST['l_name']
        email = request.POST['email']
        password = request.POST['p1']
        c_password = request.POST['p2']
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user is taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email is taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                password=password, email=email)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "password not matched")
            return redirect('register')
        return render('/')
    return render(request, "register.html")
