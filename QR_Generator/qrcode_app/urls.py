from django.urls import path
from .views import *
urlpatterns = [path("qrcode/", render_generator_qr, name = "generator_qr"),
               path("my_qrcodes", view_my_qrcodes, name = "my_qrcodes"),
               path("active/<int:id>", render_active_page, name = 'active') ]