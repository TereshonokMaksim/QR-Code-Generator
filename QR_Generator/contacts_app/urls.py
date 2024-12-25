from django.urls import path
from .views import *

urlpatterns = [
    path("contacts/", render_contacts_page, name = "contacts")
]
