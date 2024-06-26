from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Product

# Create your tests here.
class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name="Test Category", slug="test-category")

    def test_name_label(self):
        """Test whether the name label of the Category model is correctly set."""
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_slug_label(self):
        """Test whether the slug label of the Category model is correctly set."""
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field("slug").verbose_name
        self.assertEqual(field_label, "slug")
    
    def test_verbose_name_plural(self):
        """Test whether the plural verbose name of the Category model is correctly set."""
        self.assertEqual(str(Category._meta.verbose_name_plural), "categories")


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='Test Category', slug='test-category')
        Product.objects.create(category_id=1, name='Test Product', slug='test-product', price=10.99)

    def test_name_label(self):
        """Test whether the name label of the Product model is correctly set."""
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_slug_label(self):
        """Test whether the slug label of the Product model is correctly set."""
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_price_label(self):
        """Test whether the price label of the Product model is correctly set."""
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_available_default(self):
        """Test whether the default value of 'available' field in Product model is True."""
        product = Product.objects.get(id=1)
        self.assertTrue(product.available)


class ProductListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test category
        Category.objects.create(name="Test Category", slug="test-category")
        # Create test products
        Product.objects.create(category_id=1, name="Test Product 1", slug="test-product-1", price=10.99)
        Product.objects.create(category_id=1, name="Test Product 2", slug="test-product-2", price=20.99)

    def test_product_list_view_without_category(self):
        """Test the product list view without providing a category."""
        client = Client()
        response = client.get(reverse("shop:product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("shop/product/list.html")
    
    def test_product_list_view_with_valid_category(self):
        """Test the product list view with a valid category."""
        client = Client()
        category_slug = "test-category"
        response = client.get(reverse("shop:product_list_by_category", kwargs={"category_slug": category_slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/product/list.html")

    def test_product_list_view_with_invalid_category(self):
        """Test the product list view with an invalid category."""
        client = Client()
        category_slug = "invalid-category"
        response = client.get(reverse("shop:product_list_by_category", kwargs={"category_slug": category_slug}))
        self.assertEqual(response.status_code, 404) # Expecting 404 Not Found


class ProductDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test category
        Category.objects.create(name="Test Category", slug="test-category")
        # Create test products
        Product.objects.create(category_id=1, name="Test Product", slug="test-product", price=10.99)

    def test_product_detail_view_with_valid_product(self):
        """Test the product detail view with a valid product."""
        client = Client()
        product = Product.objects.get(slug="test-product")
        response = client.get(reverse("shop:product_detail", kwargs={"id": product.id, "slug": product.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/product/detail.html")
    
    def test_product_detail_view_with_invalid_product_id(self):
        """Test the product detail view with an invalid product ID."""
        client = Client()
        response = client.get(reverse("shop:product_detail", kwargs={"id": 9999, "slug": "test-product"}))
        self.assertEqual(response.status_code, 404) # Expecting 404 Not Found

    def test_product_view_with_invalid_product_slug(self):
        """Test the product detail view with an invalid product slug."""
        client = Client()
        product = Product.objects.get(slug="test-product")
        response = client.get(reverse("shop:product_detail", kwargs={"id": product.id, "slug": "invalid-slug"}))
        self.assertEqual(response.status_code, 404) # Expecting 404 Not Found