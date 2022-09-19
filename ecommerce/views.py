from django.shortcuts import render


def index(request):
    return render(request, 'pages/home/index.html')


def contact(request):
    return render(request, 'pages/contact/contact.html')
