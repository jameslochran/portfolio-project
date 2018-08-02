from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=500)
