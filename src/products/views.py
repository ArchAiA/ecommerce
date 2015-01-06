from django.shortcuts import render

# Create your views here.

from products.models import Product

def home(request):

	if request.user.is_authenticated():	
		context = {'username_is': request.user}
	else:
		context = {'username_is': request.user}

	template = 'products/home.html'
	
	return render(request, template, context)


# This method creates a view that takes every instance of the Product model
def all(request):
	products = Product.objects.all()
	context = {'all_products': products} # This takes all of the objects
	template = 'products/all.html'
	return render(request, template, context)