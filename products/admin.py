from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'public_price', 'created_at')
    list_filter = ('category', )
    search_fields = ('title__startswith', )

    def public_price(self, obj):
        """Convert price to a string with the format $XX.XX (ARS)"""
        return f"$ {obj.price}"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name__startswith', )