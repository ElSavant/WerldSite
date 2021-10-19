from django.shortcuts import render
from . import views

# Create your views here.


def about(request):
    return render(request,"team/about.html")