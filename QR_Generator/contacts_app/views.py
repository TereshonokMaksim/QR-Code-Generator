from django.shortcuts import render
from datetime import datetime, timedelta, timezone
from qrcode_app.models import QRCode
from user_app.models import Subscription, Account
# Create your views here.

def render_contacts_page(request):
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
    return render(request = request, template_name = "contacts/contacts.html")