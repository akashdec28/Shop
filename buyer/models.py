from django.db import models

# Create your models here.
class buyer_tb(models.Model):
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=6)
    dob=models.CharField(max_length=10)
    country=models.CharField(max_length=30)
    phonenumber=models.CharField(max_length=13)
    address=models.CharField(max_length=50)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
class cart_tb(models.Model):
    productid=models.ForeignKey('seller.product_tb',on_delete=models.CASCADE)
    buyerid=models.ForeignKey(buyer_tb,on_delete=models.CASCADE)
    phonenumber=models.CharField(max_length=30)
    quantity=models.IntegerField()
    shippingaddress=models.CharField(max_length=60)
    totalprice=models.IntegerField()
class order_tb(models.Model):
    buyerid=models.ForeignKey(buyer_tb,on_delete=models.CASCADE)
    shippingaddress=models.CharField(max_length=30)
    phonenumber=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    time=models.CharField(max_length=30)
    status=models.CharField(max_length=30,default="pending")
class orderitems_tb(models.Model):
    buyerid=models.ForeignKey(buyer_tb,on_delete=models.CASCADE)
    productid=models.ForeignKey('seller.product_tb',on_delete=models.CASCADE)
    orderid=models.ForeignKey(order_tb,on_delete=models.CASCADE)
    totalprice=models.CharField(max_length=30)
    quantity=models.CharField(max_length=30)
class payments_tb(models.Model):
    buyerid=models.ForeignKey(buyer_tb,on_delete=models.CASCADE)
    orderid=models.ForeignKey(order_tb,on_delete=models.CASCADE)
    cardnumber=models.CharField(max_length=30)
    cardname=models.CharField(max_length=30)
    cvd=models.CharField(max_length=30)
    expirydate=models.CharField(max_length=30)