from django.db import models

# Create your models here.
from products.models import Product


#L63: Adding Quantities to Cart App 
class CartItem(models.Model):
	#L64: Fixing Cart
	cart = models.ForeignKey('Cart', null=True, blank=True) #This comes from the Cart class
	product = models.ForeignKey(Product, null=True, blank=True) #This comes from prdocuts.Product class
	quantity = models.IntegerField(default=1)
	line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		try:
			return str(self.cart.id)
		except:
			return self.product.title	 
#L63: Adding Quantities to Cart App 


class Cart(models.Model):

	#L63: Adding Quantities to Cart App 
	#items = models.ManyToManyField(CartItem, null=True, blank=True)
	#products = models.ManyToManyField(Product, null=True, blank=True)
	#L63: Adding Quantities to Cart App

	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return "Cart ID: %s" % (self.id)


