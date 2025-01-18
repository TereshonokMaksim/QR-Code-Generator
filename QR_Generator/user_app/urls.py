from django.urls import path
from .views import *

urlpatterns = [path("logout", user_logout, name = "logout"),
               path("registration", render_register_page, name = "registration"),
               path("login", render_login_page, name = "login")]