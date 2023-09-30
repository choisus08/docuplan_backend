from django.db import models

# Create your models here.
class Appointment(models.Model):
    appointment_title = models.CharField(max_length=200)
    doctor_name = models.CharField(max_length=200)
    doctor_specialist = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    notes = models.CharField(max_length=500)