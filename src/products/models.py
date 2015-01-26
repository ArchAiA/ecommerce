#L55 Denigrated: from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=120, null=False, blank=False)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	sale_price = models.DecimalField(decimal_places=2, max_digits=100,\
										null=True, blank=True)
	slug = models.SlugField(unique=True) # A Slug Field will create urls from the title
	active = models.BooleanField(default=True)

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) # First added to database
	updated = models.DateTimeField(auto_now_add=False, auto_now=True) # Last time the instance was changed
	shipping_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True) # Unless null, and blank are both true, the attribute will be requried

	def __unicode__(self): # Every time we save the instance it will return the title as unicode
		return self.title

	class Meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price

#L55 Denigrated:	def get_absolute_url(self):
#L55 Denigrated:		return reverse("single_product", kwargs={"slug": self.slug})


class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='products/images/', null=True)
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.product.title


#L67: Managers allow you to customize our query sets
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
#L67: Managers allow you to customize our query sets


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

