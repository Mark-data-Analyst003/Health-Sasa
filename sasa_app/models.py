from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Consultation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateTimeField()
    department = models.CharField(max_length=20)
    doctor = models.CharField(max_length=20)
    message = models.TextField(default="No message provided") 

    def __str__(self):
        return f"{self.name} - {self.user.username}"

 
class SymptomsInput(models.Model):
    symptoms = models.CharField(max_length=255)  # Add max_length for CharField
    sex = models.CharField(max_length=10)       # Specify max_length based on expected input
    age = models.CharField(max_length=10, default="adult")        # Adjust max_length for age
    country = models.CharField(max_length=100)  # Set a reasonable length for country

    def __str__(self):
        return self.symptoms

class Appointment(models.Model):
    

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateTimeField()
    department = models.CharField(max_length=20)
    doctor = models.CharField(max_length=20)
    message = models.TextField(default="No message provided") 

    def __str__(self):
        return self.name
