from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.core.mail import send_mail
from django.http import HttpResponse
from QR_Generator.settings import *
from user_app.models import Subscription, Account
# Create your views here.

def render_home_page(request):
    if request.method == "POST":
        subscription = request.POST.get("subscription")
        print(request.POST)
        subscription_object = Subscription.objects.get(title = subscription)
        user = Account.objects.get(user = request.user)
        user.subscription = subscription_object
        user.save()
        subject = 'Subscription'
        message = 'Good afternoon!\nYou have sucesfully changed your subscription! You can always change it on home page.\n\nAll the best!'
        from_email =  EMAIL_HOST_USER # Отправитель
        recipient_list = [request.user.email]  # Получатель
        send_mail(subject, message, from_email, recipient_list)
    # Прописать тут условие залогинен/разлогинен
    if request.user.is_authenticated:
        return render(request = request, template_name = "home/logined.html", context = {"subscription": Account.objects.get(user = request.user).subscription.title})
    else:
        return render(request = request, template_name = "home/not_logined.html")


def is_logined(request = None):
    if request.user.is_authenticated:
        return JsonResponse(data = {"logined": request.user.username})
    else:
        return JsonResponse(data = {"logined": False})