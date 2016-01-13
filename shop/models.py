from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 200)
	parent = models.ManyToManyField("self")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Categories"

class Product(models.Model):
	name = models.CharField(max_length = 200)
	price = models.FloatField()
	description = models.TextField()
	image = models.ImageField()
	stock = models.IntegerField()
	available = models.BooleanField()

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	categories = models.ManyToManyField(Category)

	def __str__(self):
		return self.name

class Profile(models.Model):

	STATES = (
		('ACT', 'Australian Capital Territory'),
		('NSW', 'New South Wales'),
		('VIC', 'Victoria'),
		('QLD', 'Queensland'),
		('SA', 'South Australia'),
		('WA', 'Western Australia'),
		('TAS', 'Tasmania'),
		('NT', 'Northern Australia')
	)

	phone = models.CharField(max_length = 100)
	address_line_1 = models.CharField(max_length = 200)
	address_line_2 = models.CharField(max_length = 200)
	postcode = models.IntegerField()
	suburb = models.CharField(max_length = 200)
	state = models.CharField(max_length = 200, choices = STATES)
	country = models.CharField(max_length = 200, default = 'Australia')
	
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	user = models.OneToOneField(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.user.first_name

class Order(models.Model):

	STATUS = (
		('placed', 'Placed'),
		('paid', 'Paid'),
		('recieved', 'Recieved'),
		('packed', 'Packed'),
		('shipped', 'Shipped'),
		('complete', 'Complete')
	)

	status = models.CharField(max_length = 200, choices = STATUS)

	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	products = models.ManyToManyField(Product, blank = True)

	def __str__(self):
		return self.id

class Cart(models.Model):
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	user = models.OneToOneField(User, on_delete = models.CASCADE)