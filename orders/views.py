import time
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from shopping_cart.models import Cart
from .models import Order
# Create your views here.
def checkout(request):
	
	try:
		the_id=request.session['cart_id']
		cart=Cart.objects.get(id=the_id)
		print(cart)
	except:
		the_id=None
		return HttpResponseRedirect(reverse("shopping_cart:cart_list"))
	new_order, created = Order.objects.get_or_create(cart=cart)
	if created:
		new_order.order_id = str(time.time())
		new_order.save()
	if new_order.status=="Finished":
		del request.session['cart_id']
		del request.session['items_total']
		return HttpResponseRedirect(reverse("shopping_cart:cart_list"))
	context={}
	template="home.html"
	return render(request,template,context)