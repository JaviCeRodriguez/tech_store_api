from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    details = models.TextField(blank=True)
    specs = models.JSONField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.TextField(blank=True) # Imágenes separadas por comas
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='products')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-created_at']