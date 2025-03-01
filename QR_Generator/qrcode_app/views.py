from django.shortcuts import render, redirect
import qrcode.exceptions
from .models import QRCode
from user_app.models import Account, Subscription
import qrcode
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer, SquareModuleDrawer, GappedSquareModuleDrawer, RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styledpil import StyledPilImage
import os
from datetime import datetime, timedelta
# import random
from PIL import Image
import math
from django.utils import timezone


def add_center_image(image, qrcode: StyledPilImage, size: int = 10, background_color = (255, 255, 255)):
    qrcode = qrcode.convert("RGBA")
    image = Image.open(image).convert("RGBA")
    size = int(size)
    image_size = [round(qrcode.size[0] * 0.2 + size * 2), round(qrcode.size[1] * 0.2 + size * 2)]
    # print(image.size)
    image = image.resize(image_size, Image.Resampling.LANCZOS)
    # print(image.size, qrcode.size)
    actual_image = Image.new("RGB", [math.ceil(image_size[0] / size) * size, math.ceil(image_size[1] / size) * size])
    actual_image.paste(background_color, (0, 0, *actual_image.size))
    actual_image.paste(image, [round((actual_image.size[0] - image.size[0]) / 2), round((actual_image.size[1] - image.size[1]) / 2)], image)
    image_cors = [round((qrcode.size[0] - actual_image.size[0]) / 2), (qrcode.size[1] - actual_image.size[1]) // 2]
    qrcode.paste(actual_image, image_cors)
    return qrcode

def hex_to_rgb(hex: str):
    hex = hex[1:len(hex)]
    rgb_color = []
    for part in range(3):
        rgb_color.append(int(hex[part * 2], 16) * 16 + int(hex[part * 2 + 1], 16))
    return tuple(rgb_color)

def render_generator_qr(request):
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
    if request.user.is_authenticated:
        account = Account.objects.filter(user = request.user)[0]
        all_qrcodes = QRCode.objects.filter(acc_id = account)
        allowed = len(all_qrcodes) < account.subscription.max_qrcodes
        if request.method == "POST":
            if allowed:
                # print("What")
                back_color = request.POST.get("back-color")
                front_color = request.POST.get("front-color")
                size = request.POST.get("size")
                qr_code_maker = qrcode.QRCode(error_correction = qrcode.ERROR_CORRECT_H, box_size = size, border=2)
                qr_code_maker.add_data(request.POST.get("link"))
                form_style = {"round": CircleModuleDrawer, "square": SquareModuleDrawer, "rounded": RoundedModuleDrawer}[request.POST.get("form")]
                rgb_back_color = hex_to_rgb(back_color)
                if rgb_back_color == (0, 0, 0):
                    rgb_back_color = (0, 0, 1)
                img = qr_code_maker.make_image(image_factory = StyledPilImage, 
                               module_drawer = form_style(), 
                               color_mask = SolidFillColorMask(back_color=rgb_back_color, front_color=hex_to_rgb(front_color)))
                center_image = request.FILES.get("logo_image")
                if center_image:
                    img = add_center_image(image = center_image, qrcode = img, size = size, background_color = back_color)
                qrcode_model = QRCode(name = request.POST.get("name"), 
                                    size = request.POST.get("size"), 
                                    color_front = front_color[1:], 
                                    color_back = back_color[1:],
                                    form = request.POST.get("form"),
                                    link = request.POST.get("link"),
                                    path_qrcode = "on the next line",
                                    acc_id = account)   
                qrcode_model.save()
                path = os.path.abspath(__file__ + f"/../../media/images/qrcodes/{account.user.username}/")
                if not os.path.exists(path):
                    os.makedirs(path)
                now = datetime.now()
                path = f"{path}/QRCode={now.date()}_{now.hour}-{now.minute}-{now.second}={qrcode_model.id}.png"
                img.save(path) 
                qrcode_model.path_qrcode = path
                qrcode_model.save()
                return render(request = request, template_name = "generator_qr/generator_qr.html", context = {'qrcode': qrcode_model, "allowed": len(all_qrcodes) + 1 < account.subscription.max_qrcodes})
    else:
        allowed = False
    return render(request = request, template_name = "generator_qr/generator_qr.html", context = {"qrcode": False, "allowed": allowed})

def view_my_qrcodes(request):
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
        
    all_qrcodes = QRCode.objects.filter(acc_id = Account.objects.filter(user = request.user)[0])
    names_list = {}
    date_list = []
    for qrcode in all_qrcodes:
        if qrcode.name.lower() not in names_list.keys():
            names_list.update({qrcode.name.lower(): [qrcode.pk]})
        else:
            names_list[qrcode.name.lower()].append(qrcode.pk)
        date_list.append([qrcode.when_created, qrcode.pk])
    names_sorted_names = [name for name in names_list.keys()]
    names_sorted_names = sorted(names_sorted_names)
    date_list.sort()
    # print(names_sorted_names)
    names_sorted_ids = [id_qrcode for name in names_sorted_names for id_qrcode in names_list[name]]
    date_sorted_ids = [date[1] for date in date_list]
    # print(f"Names: {names_sorted_ids}/{names_list}")
    
    return render(request, "my_qrcodes.html", context = {"all_qrcodes": all_qrcodes, "names_sorted_ids": names_sorted_ids, "date_sorted_ids": date_sorted_ids})
    
def render_active_page(request, id):
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
    verifiable_qrcode = QRCode.objects.get(id = id)
    if verifiable_qrcode.active == True:
        if request.method == "GET":
            if verifiable_qrcode.link[:4] == "http":
                return redirect(verifiable_qrcode.link)
            else:
                return render(request, "active.html", context = {"not_link": verifiable_qrcode.link})
    else:
        return render(request, "active.html",context={"not_active": 1})
            