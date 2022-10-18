from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    details = models.TextField(blank=True)
    specs = models.JSONField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.TextField(blank=True) # Imágenes separadas por comas
    created_at = models.DateTimeField(auto_now_add=True)