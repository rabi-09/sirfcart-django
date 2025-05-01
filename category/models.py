from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    category_slug = models.SlugField(max_length=50)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='photos/category', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'
    
    def get_url(self):
        return reverse('shop_by_category', args=[self.category_slug])

    def __str__(self):
        return self.name
    
