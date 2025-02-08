from django.shortcuts import render
from .models import QRCode
from user_app.models import Account
import qrcode
import os


def render_generator_qr(request):
    if request.user.is_authenticated:
        account = Account.objects.filter(user = request.user)[0]
        all_qrcodes = QRCode.objects.filter(acc_id = account)
        allowed = len(all_qrcodes) < account.subscription.max_qrcodes
        if request.method == "POST":
            if allowed:
                print("What")
                img = qrcode.make(request.POST.get("link"))
                qrcode_model = QRCode(name = request.POST.get("name"), 
                                    size = request.POST.get("size"), 
                                    color = request.POST.get("color")[1:len(request.POST.get("color"))], 
                                    form = request.POST.get("form"),
                                    link = request.POST.get("link"),
                                    path_qrcode = "on the next line",
                                    acc_id = account)   
                qrcode_model.save()
                img.save(os.path.abspath(__file__ + f"/../../media/images/qrcodes/{qrcode_model.id}.png")) 
                qrcode_model.path_qrcode = f"images/qrcodes/{qrcode_model.id}.png"
                qrcode_model.save()
                return render(request = request, template_name = "generator_qr/generator_qr.html", context = {'qrcode': qrcode_model, "allowed": len(all_qrcodes) + 1 < account.subscription.max_qrcodes})
    else:
        allowed = False
    return render(request = request, template_name = "generator_qr/generator_qr.html", context = {"qrcode": False, "allowed": allowed})

def view_my_qrcodes(request):
    all_qrcodes = QRCode.objects.filter(acc_id = Account.objects.filter(user = request.user)[0])
    return render(request, "my_qrcodes.html", context = {"all_qrcodes": all_qrcodes})

