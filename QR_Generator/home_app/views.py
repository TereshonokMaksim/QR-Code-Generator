from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.core.mail import send_mail
from django.http import HttpRequest
from QR_Generator.settings import *
from user_app.models import Subscription, Account
from datetime import datetime, timedelta
from .utils import auto_check_sub
from qrcode_app.models import QRCode
# Create your views here.

def change_activation(max_qrcodes: int, user_acc: Account):
    all_qrcodes = list(QRCode.objects.filter(acc_id = user_acc))
    for qrcode in all_qrcodes:
        qrcode.active = 1
        qrcode.save()
    if len(all_qrcodes) > max_qrcodes:
        newest_qrcodes = all_qrcodes[-max_qrcodes:]
        for activated_qrcode in newest_qrcodes:
            all_qrcodes.remove(activated_qrcode)
        for qrcode in all_qrcodes:
            qrcode.active = 0
            qrcode.save()

def render_home_page(request: HttpRequest) -> None:
    auto_check_sub(user = request.user)
    if request.method == "POST":
        subscription = request.POST.get("subscription")
        print(request.POST)
        subscription_object = Subscription.objects.get(title = subscription)
        user = Account.objects.get(user = request.user)
        user.subscription = subscription_object
        change_activation(max_qrcodes = subscription_object.max_qrcodes, user_acc = user)
        user.sub_expire = datetime.now() + timedelta(28)
        user.save()
        subject = 'Subscription'
        message = f'Good afternoon!\nYou have sucesfully changed your subscription to {subscription}! You can always change it on home page.\n\nAll the best!'
        from_email =  EMAIL_HOST_USER # Отправитель
        recipient_list = [request.user.email]  # Получатель
        send_mail(subject, message, from_email, recipient_list)
        changed_sub = True
    else:
        changed_sub = False
    # Прописать тут условие залогинен/разлогинен
    if request.user.is_authenticated:
        user = Account.objects.get(user = request.user)
        print(user.sub_expire)
        return render(request = request, template_name = "home/logined.html", context = {"subscription": Account.objects.get(user = request.user).subscription.title, "changed": changed_sub})
    else:
        return render(request = request, template_name = "home/not_logined.html")


def is_logined(request = None):
    if request.user.is_authenticated:
        return JsonResponse(data = {"logined": request.user.username})
    else:
        return JsonResponse(data = {"logined": False})