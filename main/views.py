from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    banner = Banner.objects.all()
    about = About.objects.all()
    content = {'banner': banner, 'about':about}
    return render(request, 'index.html', content)

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def price(request):
    return render(request, 'price.html')

def contact(request):
    return render(request, 'contact.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def appointment(request):
    return render(request, 'appointment.html')

def search(request):
    return render(request, 'search.html')
