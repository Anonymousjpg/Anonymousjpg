from django.db import models
from products.models import Product
class  Cart (models.Model):
    products=models.ManyToManyField(Product, null=True, blank=True)
    total=models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    available = models.BooleanField(default=True)

    # def __unicode__(self):
    # 	return "Cart id: %s" %(self.id)

    def __str__(self):
        return "Cart id:{}".format(self.id)