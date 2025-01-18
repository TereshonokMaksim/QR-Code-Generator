from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.core.mail import send_mail
from django.http import HttpResponse
from QR_Generator.settings import *

# Create your views here.

def render_home_page(request):
    if request.method == "POST":
        subject = 'Subscription'
        message = 'Good afternoon!\nDid you want to subscribe? Confirm your bank card details\n\nAll the best!'
        from_email =  EMAIL_HOST_USER # Отправитель
        recipient_list = [request.user.email]  # Получатель
        send_mail(subject, message, from_email, recipient_list)
    # Прописать тут условие залогинен/разлогинен
    if request.user.is_authenticated:
        return render(request = request, template_name = "home/logined.html")
    else:
        return render(request = request, template_name = "home/not_logined.html")


def is_logined(request = None):
    if request.user.is_authenticated:
        return JsonResponse(data = {"logined": request.user.username})
    else:
        return JsonResponse(data = {"logined": False})