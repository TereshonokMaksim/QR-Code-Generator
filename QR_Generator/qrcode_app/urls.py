from django.urls import path
from .views import *
from contacts_app.views import *
urlpatterns = [path("qrcode/", render_generator_qr, name = "generator_qr"),
               
]