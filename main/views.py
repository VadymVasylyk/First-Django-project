from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def services(request):
    return render(request, 'main/services.html')
