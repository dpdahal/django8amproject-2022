from django.shortcuts import render
from .models import *


def index(request):
    data = {
        'bannerData': Banner.objects.all(),
    }
    return render(request, 'pages/home/index.html', data)


def contact(request):
    return render(request, 'pages/contact/contact.html')
