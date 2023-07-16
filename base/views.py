from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse('Home Page')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('Room Page')
    return render(request, 'about.html')

def blog(request):
    # return HttpResponse('Room Page')
    return render(request, 'blog.html')

def contact(request):
    # return HttpResponse('Room Page')
    return render(request, 'contact.html')

def dashboard(request):
    # return HttpResponse('Room Page')
    return render(request, 'dashboard.html')
