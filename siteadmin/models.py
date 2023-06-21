from django.db import models

# Create your models here.
class admin_tb(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
class category_tb(models.Model):
    name=models.CharField(max_length=25)
    
    
