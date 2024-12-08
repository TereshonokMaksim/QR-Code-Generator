from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

# Create your views here.

def render_home_page(request):
    # Прописать тут условие залогинен/разлогинен
    if request.user.is_authenticated:
        return render(request = request, template_name = "home/logined.html")
    else:
        return render(request = request, template_name = "home/not_logined.html")

def user_logout(request = None):
    logout(request = request)
    return redirect("/")

def is_logined(request = None):
    if request.user.is_authenticated:
        return JsonResponse(data = {"logined": request.user.username})
    else:
        return JsonResponse(data = {"logined": False})

def render_register_page(request):
    if request.method == "POST":
        name = str(request.POST.get("username"))
        email = request.POST.get("email")
        password = request.POST.get("password")
        for user in User.objects.all():
            
            if user.username == name:
                return render(request = request, template_name = "registration/reg.html", context = {"message": "name"})
            elif user.email == email:
                return render(request = request, template_name = "registration/reg.html", context = {"message": "email"})
        user = User.objects.create_user(username = name, email = email, password = password)
        print("created")
        return render(request = request, template_name = "registration/reg.html", context = {"message": "success"})
    return render(request = request, template_name = "registration/reg.html")

def render_login_page(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request = request, username = name, password = password)
        if user == None:
            return render(request = request, template_name = "login/log.html", context = {"message": "incorrect"})
        else:
            print("logined")
            login(request = request, user = user)
            return redirect("/") 
        
    return render(request = request, template_name = "login/log.html")