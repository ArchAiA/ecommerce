from django.db import models

from products.models import Product


class CartItem(models.Model):

	cart = models.ForeignKey('Cart', null=True, blank=True) 
	product = models.ForeignKey(Product, null=True, blank=True) 
	quantity = models.IntegerField(default=1)
	line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	notes = models.TextField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		try:
			return str(self.id)
		except:
			return self.product.title	 


class Cart(models.Model):

	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return "Cart ID: %s" % (self.id)


