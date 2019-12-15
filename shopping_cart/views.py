from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from.models import Cart
from products.models import Product
# from django.views.generic import (
# 	ListView,
# 	# DetailView,
# 	)
from .models import Cart
# class CartListView(ListView):
# 	template_name='cart/cart_list.html'
	# queryset=Cart.objects.all()[0]
def cart_view(request):
    cart=Cart.objects.all()[0]
    context = {"cart":cart}
    return render(request,"shopping_cart/cart_list.html",context)
def update_cart(request,slug):
	cart=Cart.objects.all()[0]
	product=Product.objects.get(slug=slug)
	if not product in cart.products.all():
		cart.products.add(product)
	else:
		cart.products.remove(product)
	new_total=0.00
	for item in cart.products.all():
		new_total+=float(item.price)
	cart.total=new_total
	cart.save()
	return HttpResponseRedirect(reverse('shopping_cart:cart_list'))

	# cart=Cart.objects.all()[0]
	# try:
	# 	product=Product.objects.get(slug=slug)
	# except Product.DoesNotExist:
	# 	pass
	# except:
	# 	pass
	# if not product in cart.products.all():
	# 	cart.products.add(product)
	# else:
	# 	cart.products.remove(product)
	# return HttpResponseRedirect(reverse('cart_list'))