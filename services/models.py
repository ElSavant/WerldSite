from django.db import models

# Create your models here.
class Services(models.Model):
    service_name = models.CharField(max_length=200)
    image = models.FileField(upload_to = "service_images/")
    short_description = models.TextField(max_length=200)
    long_description = models.TextField(max_length=5000)