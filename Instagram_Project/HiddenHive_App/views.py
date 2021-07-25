from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'HiddenHive_App/home.html')

def about(request):
    return render(request, 'HiddenHive_App/about.html')
