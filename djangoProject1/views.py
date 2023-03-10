from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def productpage(request):
    return render(request, 'product.html')


def contactpage(request):
    return render(request, 'contact.html')


def blogpage(request):
    return render(request, 'blog.html')


def servicespage(request):
    return render(request, 'services.html'),


def loginpage(request):
    return render(request, 'login.html')
