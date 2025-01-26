from django.shortcuts import render

def home(request):
    return render(request, 'base/index.html')

def login(request):
    return render(request, 'authentication/login.html')
