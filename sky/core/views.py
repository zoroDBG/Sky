from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def base(request):
    return redirect(request, 'base.html')

def home(request):
    return render(request, 'home.html')