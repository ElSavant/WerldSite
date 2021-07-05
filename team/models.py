from django.db import models

# Create your models here.
class Team(models.Model):
    member_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "team_images/")
    role = models.CharField(max_length=200)
    short_description = models.TextField(max_length=200)
    long_description = models.TextField(max_length=5000)
    email = models.EmailField(max_length = 254)
    contact = models.CharField(max_length=200)