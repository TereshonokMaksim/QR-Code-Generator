from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from QR_Generator.settings import *
import random
from qrcode_app.models import QRCode
from .models import Account, Subscription
from datetime import datetime, timedelta, timezone
# Create your views here.


def render_register_page(request):
    if request.user.account.sub_expire < timezone.now():
        all_qrcodes = QRCode.objects.filter(acc_id = Account.objects.filter(user = request.user)[0])
        print(all_qrcodes)
        subscription_object = Subscription.objects.filter(title = "Free")
        user = Account.objects.get(user = request.user)
        user.subscription = subscription_object
        user.save()
        newest_qrcode = all_qrcodes[-1]
        print(newest_qrcode)
        all_qrcodes.remove(newest_qrcode)
        for qrcode in all_qrcodes:
            qrcode.active = 0
            qrcode.save()
    if request.method == "POST":
       
        site_url = request.build_absolute_uri().split("/")[0:-2]
        site_url = '/'.join(site_url)
        print(site_url)
        name = str(request.POST.get("username"))
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password != password_confirm:
            return render(request = request, template_name = "registration/reg.html", context = {"message": "password"})
        for user in User.objects.all():
            
            if user.username == name:
                return render(request = request, template_name = "registration/reg.html", context = {"message": "name"})
            elif user.email == email:
                return render(request = request, template_name = "registration/reg.html", context = {"message": "email"})
        user = User.objects.create_user(username = name, email = email, password = password)
        print("created")
        verification_list = []
        for i in range(0,9,1):
            verification_list.append(str(random.randint(0, 9)))
        verification_code = ''.join(verification_list)
        account =  Account.objects.create(user = user, verified = verification_code, subscription = Subscription.objects.get(title = "Free"), sub_expire = datetime.now()+ timedelta(28))
        all_url = ''.join([site_url, account.get_absolute_url()])
        print(all_url)
       
        subject = 'Registration'
        message = f'Good day!\n Your Google account was registered on the site {all_url} .\nTo continue logging into your account, follow this link: http://127.0.0.1:8000/login \n P.S. If you were not the one logging in, just ignore this message.\n\nAll the best!'
        from_email =  EMAIL_HOST_USER # Отправитель
        recipient_list = [ request.POST.get("email")]  # Получатель
        send_mail(subject, message, from_email, recipient_list)
        
        return render(request = request, template_name = "registration/reg.html", context = {"message": "success"})
    
    return render(request = request, template_name = "registration/reg.html")

def render_login_page(request):
    if request.user.account.sub_expire < timezone.now():
        all_qrcodes = QRCode.objects.filter(acc_id = Account.objects.filter(user = request.user)[0])
        print(all_qrcodes)
        subscription_object = Subscription.objects.filter(title = "Free")
        user = Account.objects.get(user = request.user)
        user.subscription = subscription_object
        user.save()
        newest_qrcode = all_qrcodes[-1]
        print(newest_qrcode)
        all_qrcodes.remove(newest_qrcode)
        for qrcode in all_qrcodes:
            qrcode.active = 0
            qrcode.save()
   
    if request.method == "POST":
        
        name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request = request, username = name, password = password)
        if user == None:
            return render(request = request, template_name = "login/log.html", context = {"message": "incorrect"})
        else:
            account = Account.objects.get(user = user)
            if account.verified == 1:
                print("logined")
                login(request = request, user = user)
                return redirect("/") 
            else:
                 return render(request = request, template_name = "login/log.html", context = {"message": "verified"})
    return render(request = request, template_name = "login/log.html")

def user_logout(request = None):
    logout(request = request)
    return redirect("/")

def render_confirm_email_page(request, verification_code):
    if request.user.account.sub_expire < timezone.now():
        all_qrcodes = QRCode.objects.filter(acc_id = Account.objects.filter(user = request.user)[0])
        print(all_qrcodes)
        subscription_object = Subscription.objects.filter(title = "Free")
        user = Account.objects.get(user = request.user)
        user.subscription = subscription_object
        user.save()
        newest_qrcode = all_qrcodes[-1]
        print(newest_qrcode)
        all_qrcodes.remove(newest_qrcode)
        for qrcode in all_qrcodes:
            qrcode.active = 0
            qrcode.save()
    all_accounts = Account.objects.exclude(verified = 1)
    for account in all_accounts:
        if account.verified == verification_code:
            account.verified = 1
            account.save()
            print(verification_code)
    return render(request = request, template_name = "confirm_email/confirm.html")

