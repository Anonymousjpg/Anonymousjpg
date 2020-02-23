from django.db import models

# Create your models here.
from shopping_cart.models import Cart

STATUS_CHOICES=(
	("Started", "Started"),
	("Abandoned", "Abandoned"),
	("Finished", "Finished"),
	)
class Order (models.Model):
	#add users
	#add adress-maybe
	order_id=models.CharField(max_length=120, default='ABC', unique=True)
	cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
	status=models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.order_id