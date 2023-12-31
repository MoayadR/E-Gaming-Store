from django.db import models
from django.contrib.auth.models import User
import PIL


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="ProductImages/")
    def __str__(self):
        return str(self.name)

class Region(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=100)
    discount = models.IntegerField(null=True, blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="ProductImages/")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class Payment(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey( Product, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

class Cart(models.Model):
    user= models.ForeignKey( User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

class Cart_Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.cart)
