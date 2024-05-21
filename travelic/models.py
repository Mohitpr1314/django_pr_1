from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class TourPackage(models.Model):
    name = models.CharField(max_length=100)
    des = HTMLField()
    cost = models.IntegerField()

class galleryphoto(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pic')


class SaveEnquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100)
    message = models.TextField()
