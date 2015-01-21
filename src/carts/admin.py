#L60: Creating a Cart
from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
	class Meta:
		model = Cart

admin.site.register(Cart, CartAdmin)
#L60: Creating a Cart

#63: Fixing CartItem.object.get_or_create(product=product)
admin.site.register(CartItem)