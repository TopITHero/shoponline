from django.db import models
from products.models import Product
from  django.db.models.signals import post_save
# Create your models here.
class Status(models.Model):
	name = models.CharField(max_length = 24, blank = True, null = True, default = None)
	is_active = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __str__(self):

		return self.name



class Order(models.Model):
	custumer_name = models.CharField(max_length = 64, blank = True, null = True, default = None)
	custumer_email = models.EmailField(blank = True, null = True, default = None)
	customer_phone = models.CharField(max_length = 20, blank = True, null = True, default = None)
	customer_address = models.CharField(max_length = 20, blank = True, null = True, default = None)
	comments = models.TextField(blank = True, null = True, default = None)
	totalprice = models.DecimalField(max_digits = 10, decimal_places = 5, default = 0)
	status = models.ForeignKey(Status)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __str__(self):
		return "Замовлення {}".format(self.id)

	def save(self, *args, **kwargs):

		super(Order,self).save(*args, **kwargs)


class ProductInOrder(models.Model):
	order = models.ForeignKey(Order, blank = True, null = True, default = None)
	product = models.ForeignKey(Product, blank = True, null = True, default = None)
	is_active = models.BooleanField(default = True)
	number = models.IntegerField(default = 1)
	itemprice = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	totalprice = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)


	def __str__(self):
		return "Замовлення {}".format(self.product.name) 

	def save(self, *args, **kwargs):
		itemprice = self.product.price 
		self.itemprice = itemprice
		self.totalprice = self.number*self.itemprice

		super(ProductInOrder,self).save(*args, **kwargs)	

def products_in_order_post_save(sender,instance,created,**kwargs):
	order = instance.order
	all_products_in_order = ProductInOrder.objects.filter(order = order,is_active = True)
	order_total_price = 0
	for item in all_products_in_order:
		order_total_price +=item.totalprice
	instance.order.totalprice = order_total_price
	instance.order.save(force_update = True)

post_save.connect(products_in_order_post_save,sender = ProductInOrder)	


class BuyingProduct(models.Model):
	session_key = models.CharField(max_length = 250)
	Order = models.ForeignKey(Order, blank = True, null = True, default = None)
	product = models.ForeignKey(Product, blank = True, null = True, default = None)
	is_active = models.BooleanField(default = True)
	numb = models.IntegerField(default = 1)
	itemprice = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	totalprice = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)


	def __str__(self):
		return self.product.name


	def save(self, *args, **kwargs):
		
		itemprice = self.product.price 
		
		self.itemprice = itemprice
		
		self.totalprice = int(self.numb)*self.itemprice

		super(BuyingProduct,self).save(*args, **kwargs)	


