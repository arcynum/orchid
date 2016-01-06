from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length = 200)
	price = models.FloatField()
	description = models.TextField()
	image = models.ImageField()
	stock = models.IntegerField()
	available = models.BooleanField()

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

class Profile(models.Model):
	
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	user = models.OneToOneField(User, on_delete = models.CASCADE)

class Order(models.Model):

	STATUS = (
		('placed', 'Placed'),
		('paid', 'Paid'),
		('recieved', 'Recieved'),
		('packed', 'Packed'),
		('shipped', 'Shipped'),
		('complete', 'Complete')
	)

	status = models.CharField(choices = STATUS)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	products = models.ManyToManyField(Product, blank = True)

class Cart(models.Model):
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	user = models.OneToOneField(User, on_delete = models.CASCADE)