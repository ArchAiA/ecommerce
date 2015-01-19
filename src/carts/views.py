#L60: Creating a Cart
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.
from products.models import Product
from .models import Cart

def view(request):
#L61: When you want to view the cart this will first check if the_id exists
#If the_id exists, then all of the objects associated with cart where id = the_id
#will show up.  If the_id does not exist, then the_id is set to None, and the 
#cart = Cart.object.get(id = the_id) will not run, and there will be nothing to view
	try:
		the_id = request.session['cart_id']
	except:
		the_id = None
	
	if the_id:
		cart = Cart.objects.get(id = the_id)
		context = {"cart": cart}
	else:
		empty_message = "Your cart is empty, keep shopping."
		context = {"empty": True, "empty_message": empty_message}

	template = "cart/view.html"
	return render(request, template, context)



def update_cart(request, slug):
	#L61: Eliminated: cart = Cart.objects.all()[0]

#L61: Using unique sessions to manage carts
	request.session.set_expiry(1800)
	try:
		the_id = request.session['cart_id'] #L61: If cart_id exists, use it, else create cart_id
	except:
		new_cart = Cart() #L61: Create cart_id if it does not exist
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id

	cart = Cart.objects.get(id=the_id) #L61: take all of the objects in the instance of cart where the cart id = the_id


	try:
		product = Product.objects.get(slug=slug)
	except Product.DoesNotExist:
		pass
	except:
		pass
	if not product in cart.products.all(): #If the item is not in the cart add it
		cart.products.add(product)
	else:
		cart.products.remove(product) #Else remove the item

	new_total = 0.00
	for item in cart.products.all():
		new_total += float(item.price)
	cart.total = new_total
	cart.save()

	request.session['items_total'] = cart.products.count()
	print cart.products.count()

	return HttpResponseRedirect(reverse("cart")) #After any cart is updated the user will be redirected to the entry in urls.py with name="cart"
#L60: Creating a Cart
