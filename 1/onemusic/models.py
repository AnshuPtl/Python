from django.db import models

# Create your models here.
class User(models.Model):
	Name=models.CharField(max_length=50)
	PhoneNumber=models.BigIntegerField()
	Email=models.EmailField()
	Password=models.CharField(max_length=50)
	
	def __str__(self):
		return self.Name