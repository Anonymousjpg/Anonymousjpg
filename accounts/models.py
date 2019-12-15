from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from products.models import Product
# Create your models here.


class CustomUser(AbstractUser):

	def __str__(self):
		return self.username

