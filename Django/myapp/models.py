from django.db import models

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField()
	pswd=models.CharField(max_length=50)
	usertype=models.CharField(default='user',max_length=100)


	def __str__(self):
		return self.name

class Category(models.Model):
	name=models.CharField(max_length=100)

	def __str__(self):
		return self.name