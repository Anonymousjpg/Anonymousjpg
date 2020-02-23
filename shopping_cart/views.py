from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from.models import Cart
from products.models import Product
from .models import Cart

def cart_list(request):
	try:
		the_id=request.session['cart_id']
	except:
		the_id=None
	if the_id:
		cart=Cart.objects.get(id=the_id)
		context={"cart":cart}
	else:
		empty_message="Your cart is empty"
		context={"empty":True,"empty_message":empty_message}

	template='shopping_cart/cart_list.html'
	return render(request, template, context)

def update_cart(request,id):
	request.session.set_expiry(1800) #pół ghodziny
	try:
		the_id=request.session['cart_id']
	except:
		new_cart=Cart()
		new_cart.save()
		request.session['cart_id']=new_cart.id
		the_id=new_cart.id
	cart=Cart.objects.get(id=the_id)

	product=Product.objects.get(id=id)
	if not product in cart.products.all():
		cart.products.add(product)
	else:
		cart.products.remove(product)
	new_total=0.00
	for item in cart.products.all():
		new_total+=float(item.price)
	request.session['items_total'] = cart.products.count()
	print(cart.products.count())
	cart.total=new_total
	cart.save()
	return HttpResponseRedirect(reverse('shopping_cart:cart_list'))
