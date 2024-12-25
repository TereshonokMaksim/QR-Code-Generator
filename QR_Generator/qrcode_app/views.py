from django.shortcuts import render
from .models import QRCode
# Create your views here.


def render_generator_qr(request):
    return render(request = request, template_name = "generator_qr/generator_qr.html")

def view_my_qrcodes(request):
    all_qrcodes = QRCode.objects.all()
    return render(request, "my_qrcodes.html", context = {"all_qrcodes": all_qrcodes} )