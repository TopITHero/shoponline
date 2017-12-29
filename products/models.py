from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 64, blank = True, null = True, default = None)
	description = models.TextField(blank = True, null = True, default = None)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

class Product(models.Model):
	name = models.CharField(max_length = 64, blank = True, null = True, default = None)
	description = models.TextField(blank = True, null = True, default = None)
	is_active = models.BooleanField(default = True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __str__(self):
		return self.name
	def save(self, *args, **kwargs):
		print("working")
		super(Product,self).save(*args, **kwargs)	


class ProductImage(models.Model):
	product = models.ForeignKey(Product, blank = True, null = True, default = None)
	categoty = models.ForeignKey(Category, blank = True, null = True, default = None)
	image = models.ImageField()
	is_main = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __str__(self):
		return self.product.name		