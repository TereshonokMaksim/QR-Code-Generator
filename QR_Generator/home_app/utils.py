from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AnonymousUser
from user_app.models import Subscription, Account
from django.utils import timezone
from datetime import timedelta
from qrcode_app.models import QRCode


def auto_check_sub(user: User):
    '''
        Проверяет, действительна ли подписка пользователя
    '''
    if isinstance(user, User):
        user_acc = Account.objects.get(user = user)
        if user_acc.sub_expire < timezone.now():
            all_qrcodes = list(QRCode.objects.filter(acc_id = user_acc))
            subscription_object = Subscription.objects.get(title = "Free")
            user_acc.subscription = subscription_object
            user_acc.sub_expire = timezone.now() + timedelta(28)
            user_acc.save()
            if len(all_qrcodes) > 0:
                newest_qrcode = all_qrcodes[-1]
                all_qrcodes.remove(newest_qrcode)
                for qrcode in all_qrcodes:
                    qrcode.active = 0
                    qrcode.save()