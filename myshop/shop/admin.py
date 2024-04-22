from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for Category model."""

    # Display fields in the list view
    list_display = ["name", "slug"]

    # Automatically generate slug based on the name
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin configuration for Product model"""

    # Display fields in the list view
    list_display = ["name", "slug", "price",
                    "available", "created", "updated"]
    
    # Add filters for available, created, and updated fields
    list_filter = ["available", "created", "updated"]

    # Allow editing price and availability directly from the list view
    list_editable = ["price", "available"]

    # Automatically generate slug based on the name
    prepopulated_fields = {"slug": ("name",)}



