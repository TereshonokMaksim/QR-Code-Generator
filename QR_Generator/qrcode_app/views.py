from django.shortcuts import render

# Create your views here.

def render_generator_qr(request):
    return render(request = request, template_name = "generator_qr/generator_qr.html")