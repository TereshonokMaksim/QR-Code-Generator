from django.urls import path
from .views import *
from contacts_app.views import *
urlpatterns = [path("", render_home_page, name = "home"),
               path("logout", user_logout, name = "logout"),
               path("registration", render_register_page, name = "registration"),
               path("login", render_login_page, name = "login"),
               path("is_logined", is_logined, name = "is_logined")]