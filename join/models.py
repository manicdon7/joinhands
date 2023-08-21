from django.db import models

class Res(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurant_images/')
    status = models.CharField(max_length=20, default='Not Claimed')

class Sign(models.Model):
    user = models.CharField(max_length=150)
    password= models.CharField(max_length=50)
    DESIGNATION_CHOICES = (
        ('NGO', 'NGO'),
        ('Restaurant', 'Restaurant'),
    )
    designation = models.CharField(max_length=10, choices=DESIGNATION_CHOICES, default='NGO')
class Login(models.Model):
    user= models.CharField(max_length=100)
    password= models.CharField(max_length=50)