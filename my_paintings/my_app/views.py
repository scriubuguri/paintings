from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"

def about_me(request):
    return render(request, 'my_app/about_me.html')

def my_paintings(request):
    return render(request, 'my_app/my_paintings.html')

def my_tools(request):
    return render(request, 'my_app/my_tools.html')
