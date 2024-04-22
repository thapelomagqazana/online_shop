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
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_slug_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field("slug").verbose_name
        self.assertEqual(field_label, "slug")
    
    def test_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), "categories")

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='Test Category', slug='test-category')
        Product.objects.create(category_id=1, name='Test Product', slug='test-product', price=10.99)

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_slug_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_available_default(self):
        product = Product.objects.get(id=1)
        self.assertTrue(product.available)


class ProductListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test category
        Category.objects.create(name="Test Category", slug="test-category")
        # Create test products
        Product.objects.create(name="Test Product 1", slug="test-product-1", price=10.99)
        Product.objects.create(name="Test Product 2", slug="test-product-2", price=20.99)

    def test_product_list_view(self):
        client = Client()
        response = client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)