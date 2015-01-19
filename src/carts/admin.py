#L60: Creating a Cart
from django.contrib import admin

# Register your models here.
from .models import Cart

class CartAdmin(admin.ModelAdmin):
	class Meta:
		model = Cart

admin.site.register(Cart, CartAdmin)
#L60: Creating a Cart
