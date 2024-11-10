from ast import mod
from turtle import up
from django.db import models

# Create your models here.
class Students (models.Model):
    first_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, blank=True)
    email= models.EmailField(max_length=50, unique=True)
    primary_skill = models.CharField(max_length=50)
    addl_skill = models.CharField(max_length=50)
    activation_code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # photo = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return self.first_name
    