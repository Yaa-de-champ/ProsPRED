from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import numpy as np
from .forms import ImageUploadForm
from tensorflow.keras.models import load_model


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
            
# Load the pre-trained model (replace with your filename and path)
model = load_model(r"C:\Users\Lenovo\Downloads\model.h5")

def upload_view(request):
    if request.method == 'POST':
        # Handle file upload logic
        uploaded_file = request.FILES['image']
        # ... (data pre-processing logic for your 3D image data)

        # Make prediction using the loaded model
        prediction = model.predict(uploaded_file)
        predicted_class = np.argmax(prediction)  # Assuming binary classification

        # ... (logic to handle and display the prediction result)

        # Optionally, save the prediction for further use (requires a model)
        # prediction_obj = Prediction.objects.create(image=uploaded_file, predicted_class=predicted_class)

    return render(request, 'results.html', context={'prediction': predicted_class})
# ... (GET request handling logic for the upload form)
