from django.shortcuts import render
from .models import QRCode
# Create your views here.

def view_my_qrcodes(request):
    all_qrcodes = QRCode.objects.all()
    return render(request, "my_qrcodes.html", context = {"all_qrcodes": all_qrcodes})