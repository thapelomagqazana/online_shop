from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def product_list(request, category_slug=None):
    """View function to display a list of products.

    Args:
        request: The HTTP request object.
        category_slug (optional): The slug of the category to filter products by. Defaults to None.

    Returns:
        The rendered HTML template with the list of products.
    """
    category = None
    categories = Category.objects.all() # Get all categories
    products = Product.objects.filter(available=True) # Get all available products

    # If a category_slug is provided, filter products by category
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  "shop/product/list.html",
                  {"category" : category,
                   "categories" : categories,
                   "products": products})

def product_detail(request, id, slug):
    """View function to display the details of a product.

    Args:
        request: The HTTP request object
        id: The ID of the product. 
        slug: The slug of the product. 

    Returns:
        The rendered HTML template with the product details.
    """
    # Get the product object with the given id and slug
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    
    return render(request,
                  "shop/product/detail.html",
                  {"product": product})
