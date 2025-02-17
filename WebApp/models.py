from django.db import models

# Create your models here.
class contactDB(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Subject=models.EmailField(max_length=100,null=True,blank=True)
    Phone=models.ImageField(null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
class RegisterDB(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Confirm_password=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
class sign_upDB(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Confirm_password=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
class cartDB(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Product_name=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Total_price=models.IntegerField(null=True,blank=True)
    Product_image=models.ImageField(upload_to="Cart", null=True, blank=True)
class checkoutDB(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100, null=True, blank=True)
    Address=models.CharField(max_length=300, null=True, blank=True)
    Place=models.CharField(max_length=100, null=True, blank=True)
    Pincode=models.IntegerField( null=True, blank=True)
    Phone=models.IntegerField( null=True, blank=True)
    Amount=models.IntegerField( null=True, blank=True)
    Message=models.CharField(max_length=300, null=True, blank=True)