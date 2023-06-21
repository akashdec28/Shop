from django.db import models

# Create your models here.
class seller_tb(models.Model):
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=6)
    dob=models.CharField(max_length=10)
    country=models.CharField(max_length=30)
    phonenumber=models.CharField(max_length=13)
    address=models.CharField(max_length=50)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    file=models.FileField()
    status=models.CharField(max_length=30,default="pending")
class media_tb(models.Model):
    file=models.FileField()
class product_tb(models.Model):
    productname=models.CharField(max_length=30)
    productimage=models.FileField()
    productprice=models.IntegerField()
    productdetails=models.CharField(max_length=30)
    productstock=models.IntegerField()
    sellerid=models.ForeignKey(seller_tb,on_delete=models.CASCADE)
    categoryid=models.ForeignKey('siteadmin.category_tb',on_delete=models.CASCADE)
class tracking_tb(models.Model):
    orderid=models.ForeignKey('buyer.order_tb',on_delete=models.CASCADE)
    date=models.CharField(max_length=30)
    time=models.CharField(max_length=30)
    discription=models.CharField(max_length=30)
    
    
    
