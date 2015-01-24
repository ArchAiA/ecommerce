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
	#If you use ForeignKey with products, then you can only put one product in the cart
	#If you use ManyToMany instead, you can put multiple items in the cart
	#products = models.ForeignKey(Product, null=True, blank=True) #This is a ManyToMany field because the variable products will hold multiple values, each of which will be an instance of Product
	#L63: Adding Quantities to Cart App

	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return "Cart ID: %s" % (self.id)


