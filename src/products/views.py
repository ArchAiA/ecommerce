from django.shortcuts import render, Http404

# Create your views here.

from .models import Product, ProductImage
#from .models import ProductImage #L56: Alternate method of setting images in view single

def home(request):
	products = Product.objects.all()
	template = 'products/home.html'
	context = {"products": products}
	return render(request, template, context)


# This method creates a view that takes every instance of the Product model
def all(request):
	products = Product.objects.all() # Each object in products is stored in variable products
	context = {'all_products': products} # This takes all of the objects and associates them with a dictionary key 
	template = 'products/all.html'
	return render(request, template, context)


def single(request, slug): #L54: We add that slug will be an argument passed to the view
	try:
		product = Product.objects.get(slug=slug)
		#images = product.productimage_set.all()
		images = ProductImage.objects.filter(product=product) #L56: Alternate method of setting images in view single
		#L54 Eliminated: products = Product.objects.all() # Each object in products is stored in variable products
		context = {'product': product, 'images': images} # This takes all of the objects and associates them with a dictionary key 
		template = 'products/single.html'
		return render(request, template, context)
	except:
		raise Http404

#L57: Adding a view for the search
def search(request):
	try:
		q = request.GET.get('q')
	except:
		q=None
	if q:
		products = Product.objects.filter(title__icontains=q)
		template = 'products/results.html'
		context = {'query': q, 'products': products}
	else:
		template = 'products/home.html'
		context = {}
	return render(request, template, context)
