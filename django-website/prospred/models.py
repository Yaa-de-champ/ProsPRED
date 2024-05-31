from django.db import models

# Create your models here.
from django.db import models

class Prediction(models.Model):
    image = models.ImageField(upload_to='uploads/')  # Adjust upload path
    predicted_class = models.CharField(max_length=255)  # Clinically significant/insignificant
    prediction_date = models.DateTimeField(auto_now_add=True)
