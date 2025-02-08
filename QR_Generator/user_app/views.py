from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from QR_Generator.settings import *
from .models import Account, Subscription
import random
# Create your views here.


def render_register_page(request):
    if request.method == "POST":
       
         
        name = str(request.POST.get("username"))
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        for user in User.objects.all():
            if user.username == name:
                return render(request = request, template_name = "registration/reg.html", context = {"message": "name"})
            elif user.email == email:
                return render(request = request, template_name = "registration/reg.html", context = {"message": "email"})
        if password != password_confirm:
            return render(request = request, template_name = "registration/reg.html", context = {"message": "password"})
        user = User.objects.create_user(username = name, email = email, password = password)
        print("created")
        Account.objects.create(user = user, 
                                 verified = int("".join([str(random.randint(0, 9)) for repeater in range(10)])), 
                               subscription = Subscription.objects.filter(title = "Free")[0])
        subject = 'Registration'
        message = 'Good day!\n Your Google account was registered on the site http://127.0.0.1:8000/ .\nTo continue logging into your account, follow this link: http://127.0.0.1:8000/login \n P.S. If you were not the one logging in, just ignore this message.\n\nAll the best!'
        from_email =  EMAIL_HOST_USER # Отправитель
        recipient_list = [request.POST.get("email")]  # Получатель
        send_mail(subject, message, from_email, recipient_list)
        
        return render(request = request, template_name = "registration/reg.html", context = {"message": "success"})
    
    return render(request = request, template_name = "registration/reg.html")

def render_login_page(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request = request, username = name, password = password)
        if user == None:
            return render(request = request, template_name = "login/log.html", context = {"message": "incorrect"})
        else:
            print("logined")
            login(request = request, user = user)
            return redirect("/") 
        
    return render(request = request, template_name = "login/log.html")

def user_logout(request = None):
    logout(request = request)
    return redirect("/")