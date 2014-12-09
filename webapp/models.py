from django.db import models


# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    disease = models.CharField(max_length=50)
    last_visit = models.DateField()
    
    
class SensorReading(models.Model):
    patient = models.ForeignKey(Patient)
    reading_time = models.DateField()
    sensor_type = models.CharField(max_length=50)
    reading_value = models.PositiveIntegerField()
   
