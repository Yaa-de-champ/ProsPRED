from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse('Hello World')

def home(request):
    return render (request, 'index.html')

def about(request):
    return render (request, 'about.html')

def register(request):
    if request.method == "POST":
    # perform registration logic here
        pass
    return render (request, 'register.html')