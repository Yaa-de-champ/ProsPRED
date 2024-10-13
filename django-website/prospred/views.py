from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# import numpy as np
# from .forms import ImageUploadForm
# from .models import load_model
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

# def predict(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = request.FILES['image']
            
            