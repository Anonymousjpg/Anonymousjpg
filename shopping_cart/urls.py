from django.urls import path
# from .views import (CartListView)
from .views import (cart_list)

# Cart Urls
app_name='shopping_cart'
urlpatterns = [
    path('',cart_list, name='cart_list')
    ]

