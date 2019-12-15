from django.urls import path
# from .views import (CartListView)
from .views import (cart_view)

# Cart Urls
app_name='shopping_cart'
urlpatterns = [
    path('',cart_view, name='cart_list'),
    ]
# path('',CartListView(), name='cart_list'),
# path('cart/(?P<slug>[\w-]+)/$',update_cart, name='update_cart')