from django.db import models
from phone_field import PhoneField

class MenuItem(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to = 'menu_images/')
	price = models.DecimalField(max_digits=5, decimal_places=0)
	category = models.ManyToManyField('Category', related_name='item')

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class OrderModel(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(max_digits=7, decimal_places=0)
	items = models.ManyToManyField('MenuItem', related_name='order', blank=True)
	name = models.CharField(max_length=50, blank=True)
	email = models.CharField(max_length=50, blank=True)
	phone = PhoneField(blank=True)
	street = models.CharField(max_length=50, blank=True)
	city = models.CharField(max_length=50, blank=True)
	is_paid = models.BooleanField(default=False)
	is_shipped = models.BooleanField(default=False)
	

	def __str__(self):
		return f'order: {self.created_on.strftime("%b %d %I: %M %p")}'
