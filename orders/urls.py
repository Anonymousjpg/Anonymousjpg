from django.urls import path
# from .views import (CartListView)
from .views import (checkout)
# Cart Urls
app_name='orders'
urlpatterns = [
    path('',checkout, name='checkout')
    ]