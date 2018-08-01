from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=72, blank=True)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    pub_date = models.DateTimeField()
