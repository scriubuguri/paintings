from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_home_page(request):
    return HttpResponse("<h1>Hellooo human being!</h1>")
