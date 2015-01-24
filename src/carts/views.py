#L60: Creating a Cart
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.
from products.models import Product
from .models import Cart, CartItem

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

#L65: Adding quantities to the add to cart
	try:
		qty = request.GET.get('qty')
		update_qty = True
	except:
		qty = None
		update_qty = False
	
	try:
		attr = request.GET.get("attr")
	except:
		attr = None

	print attr
#L65: Adding quantities to the add to cart



	#L61: Eliminated: cart = Cart.objects.all()[0]

#L61: Using unique sessions to manage carts
	request.session.set_expiry(1800)
#L61: Check to see if cart_id exists, and create cart_id if it does not exist
	try:
		the_id = request.session['cart_id'] #L61: If cart_id exists, use it, else create cart_id
	except:
		new_cart = Cart() #new_cart is a new instand of Cart()
		new_cart.save() #Save instance new_cart
		request.session['cart_id'] = new_cart.id #Set the session value for key 'cart_id' to new_cart.id
		the_id = new_cart.id
#L61: Check to see if cart_id exists, and create cart_id if it does not exist

	cart = Cart.objects.get(id=the_id) #L61: Set cart equal to the instance of Cart where id=the_id

	try:
		product = Product.objects.get(slug=slug)
	except Product.DoesNotExist:
		pass
	except:
		pass

	#cart_item (a cart, and item combination) is equal to an objtect in CartItem where cart = cart, and product = product
	cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product) #L62: Creates a tuple that returns ("cart item object", "True/False")
	if created: 
		print "yeah"

	if update_qty and qty:
		if int(qty) == 0:
			cart_item.delete()
		else:
			cart_item.quantity = qty
			cart_item.save()
	else:
		pass

# L64: This is no longer needed because adding cart=cart to teh cart_item assignment
# 	  makes this unnecessary
# 	if not cart_item in cart.items.all(): #If the item is not in the cart add it
# 		cart.items.add(cart_item)
# 	else:
# 		cart.items.remove(cart_item) #Else remove the item
# L64: This is no longer needed because adding cart=cart to teh cart_item assignment

	new_total = 0.00
	for item in cart.cartitem_set.all(): #L64: This ...
		line_total = float(item.product.price) * item.quantity
		new_total += line_total

	request.session['items_total'] = cart.cartitem_set.count()
	cart.total = new_total
	cart.save()

	print cart.cartitem_set.count()

	return HttpResponseRedirect(reverse("cart")) #After any cart is updated the user will be redirected to the entry in urls.py with name="cart"
#L60: Creating a Cart
