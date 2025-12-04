from django.db import models

class Users(models.Model):
    UserName=models.CharField(max_length=50)
    email= models.EmailField()
    password= models.CharField(max_length=6)

class Orders(models.Model):
    customer_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity= models.IntegerField()

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)