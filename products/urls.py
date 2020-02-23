from django.urls import path
from .views import (product_list, ProductDetailView)
app_name='products'
urlpatterns=[
path('',product_list, name='products'),
path(r'^(?P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),
path('<int:id>',ProductDetailView.as_view(), name='product_detail'),

]
