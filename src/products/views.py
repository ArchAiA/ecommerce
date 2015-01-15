from django.shortcuts import render, Http404

# Create your views here.

from products.models import Product

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
		#L54 Eliminated: products = Product.objects.all() # Each object in products is stored in variable products
		context = {'product': product} # This takes all of the objects and associates them with a dictionary key 
		template = 'products/single.html'
		return render(request, template, context)
	except:
		raise Http404
