from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

from products.models import Product
from .models import Cart, CartItem

def view(request):

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

	try:
		qty = request.GET.get('qty')
		update_qty = True
	except:
		qty = None
		update_qty = False


	notes = {}
	try:
		color = request.GET.get("color")
		notes['color'] = color
	except:
		color = None

	try:
		size = request.GET.get("size")
		notes['size'] = size
	except:
		size = None		

	request.session.set_expiry(1800)
	try:
		the_id = request.session['cart_id'] 
	except:
		new_cart = Cart() 
		new_cart.save() 
		request.session['cart_id'] = new_cart.id 
		the_id = new_cart.id


	cart = Cart.objects.get(id=the_id) 

	try:
		product = Product.objects.get(slug=slug)
	except Product.DoesNotExist:
		pass
	except:
		pass

	cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
	if created: 
		print "yeah"

	if update_qty and qty:
		if int(qty) == 0:
			cart_item.delete()
		else:
			cart_item.quantity = qty
			cart_item.notes = notes
			cart_item.save()
	else:
		pass

	new_total = 0.00
	for item in cart.cartitem_set.all(): 
		line_total = float(item.product.price) * item.quantity
		new_total += line_total

	request.session['items_total'] = cart.cartitem_set.count()
	cart.total = new_total
	cart.save()

	print cart.cartitem_set.count()

	return HttpResponseRedirect(reverse("cart")) 