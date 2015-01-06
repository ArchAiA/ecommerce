from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=120, null=False, blank=False)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	sale_price = models.DecimalField(decimal_places=2, max_digits=100,\
										null=True, blank=True)
	image = models.FileField(upload_to='products/images/', null=True)
	slug = models.SlugField() # A Slug Field will create urls from the title
	active = models.BooleanField(default=True)

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) # First added to database
	update = models.DateTimeField(auto_now_add=False, auto_now=True) # Last time the instance was changed
	shipping_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True) # Unless null, and blank are both true, the attribute will be requried

	def __unicode__(self): # Every time we save the instance it will return the title as unicode
		return self.title

	def get_price(self):
		return self.price


