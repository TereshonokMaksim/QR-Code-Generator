from django.urls import path
from .views import *
urlpatterns = [path("", render_home_page, name = "home"),
               path("is_logined", is_logined, name = "is_logined")]