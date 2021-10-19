from django.shortcuts import render
from services.models import Services

# Create your views here.
def home(request):
    service = Services.objects
    return render(request,"services/home.html",{"services":service})

def services(request):
    service = Services.objects
    return render(request,"services/services.html",{"services":service})