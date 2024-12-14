from django.urls import path
from .views import *

urlpatterns = [ path("my_qrcodes", view_my_qrcodes, name = "my_qrcodes")]
