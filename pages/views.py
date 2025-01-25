from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeViewPage(request):
    return HttpResponse("<h1>Hello World</h1><h2>Welcome to Django</h2><h2>Home Page</h2>")