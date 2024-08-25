from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	mobile=models.IntegerField()
	address=models.TextField()
	email=models.EmailField()
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default="user")

	def __str__(self):
		return self.fname+" "+self.lname 

class Product(models.Model):
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_name=models.CharField(max_length=100)
	product_price=models.IntegerField()
	product_qty=models.IntegerField()
	product_desc=models.TextField()
	product_image=models.ImageField(upload_to="product_image/")
	product_venue=models.TextField(default="")
	product_time=models.TimeField(blank=True,null=True)
	product_date=models.DateField(blank=True,null=True)

	def __str__(self):
		return self.seller_fname+" - "+self.product_name

class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.fname+" - "+self.product.product_name
