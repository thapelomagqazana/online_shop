from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    """Model representing a product category."""
    name = models.CharField(max_length=200,
                            help_text="Enter the category name.")
    slug = models.SlugField(max_length=200,
                            unique=True,
                            help_text="Unique URL path to access this category.")
    
    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        """String for representing the Category object."""
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:product_list_by_category",
                       args=[self.slug])


class Product(models.Model):
    """Model representing a product."""
    category = models.ForeignKey(Category,
                                 related_name="products",
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, 
                            help_text="Enter the product name.")
    slug = models.SlugField(max_length=200, 
                            help_text="Unique URL path to access this product.")
    image = models.ImageField(upload_to="products/%Y/%m/%d",
                              blank=True,
                              help_text="Product image.")
    description = models.TextField(blank=True,
                                   help_text="Description of the product.")
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                help_text="Price of the product.")
    available = models.BooleanField(default=True, 
                                    help_text="Indicates whether the product is available for purchase.")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        """String for representing the Product object."""
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:product_detail",
                       args=[self.id, self.slug])
