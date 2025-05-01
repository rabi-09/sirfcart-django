from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='photos/products', blank=True)
    stock = models.PositiveIntegerField()
    is_availabel = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add =True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'products'
        verbose_name_plural = 'Products'

    def get_url(self):
        return reverse('product', args=[self.category.category_slug, self.product_slug])

    def __str__(self):
        return self.product_name