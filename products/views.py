from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views.generic import (
	ListView,
	DetailView,
	)
# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'products/product_list.html', context)

# class ProductListView(ListView):
# 	queryset=Product.objects.filter(available=True)

class ProductDetailView(DetailView):
	def get_object(self):
		id_=self.kwargs.get("id")
		return get_object_or_404(Product, id=id_)
