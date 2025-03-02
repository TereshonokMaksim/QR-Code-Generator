from django.shortcuts import render
from home_app.utils import auto_check_sub
from django.http import HttpRequest
# Create your views here.

def render_contacts_page(request: HttpRequest):
    auto_check_sub(user = request.user)
    return render(request = request, template_name = "contacts/contacts.html")