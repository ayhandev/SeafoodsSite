from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class info(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=355)

class FormsRegister(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=355)

class EmailRegister(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class VisitCounter(models.Model):
    count = models.PositiveIntegerField(default=0)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="media/")
    region = models.CharField(max_length=100, null=True)
    user = models.CharField(max_length=100, null=True) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name



class Review(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name


class VIPStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_vip = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username