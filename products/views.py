from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import (
	ListView,
	DetailView,
	)
# Create your views here.
class ProductListView(ListView):
	queryset=Product.objects.all()

class ProductDetailView(DetailView):
	def get_object(self):
		id_=self.kwargs.get("id")
		return get_object_or_404(Product, id=id_)