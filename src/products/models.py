from django.db import models


class Product(models.Model):
	title = models.CharField(max_length=120, null=False, blank=False)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	sale_price = models.DecimalField(decimal_places=2, max_digits=100,\
										null=True, blank=True)
	slug = models.SlugField(unique=True) 
	active = models.BooleanField(default=True)

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) 
	updated = models.DateTimeField(auto_now_add=False, auto_now=True) 
	shipping_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True) 
	def __unicode__(self): 
		return self.title

	class Meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price

class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='products/images/', null=True)
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.product.title


class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)
	def sizes(self):
		return self.all().filter(category='size')
	def trims(self):
		return self.all().filter(category='trim')


VAR_CATEGORIES = (
	('size', 'size'),
	('color', 'color'),
	('package', 'package'),
	('trim', 'trim'),
	)


class Variation(models.Model):

	category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
	product = models.ForeignKey(Product)
	title = models.CharField(max_length=120)
	image = models.ForeignKey(ProductImage, null=True, blank=True)
	price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
	objects = VariationManager()

	
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.title

