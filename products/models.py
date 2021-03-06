from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])

class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', default=None, on_delete=models.CASCADE)
	title=models.CharField(max_length=120, db_index=True) 
	slug = models.SlugField(max_length=100, db_index=True)
	description=models.TextField(blank=True, null=True)
	price=models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	image = models.ImageField(upload_to='static/img/', default=False)
	stock=models.PositiveSmallIntegerField()
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	def get_absolute_url(self):
		return f"/products/{self.id}"


	class Meta:
		ordering = ('title', )
		index_together = (('id', 'slug'),)
	def __str__(self):
		return self.title