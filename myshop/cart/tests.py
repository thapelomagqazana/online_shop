# from django.test import TestCase, RequestFactory
# from django.conf import settings
# from django.urls import reverse
# from shop.models import Product, Category
# from .cart import Cart
# from .views import cart_add, cart_remove, cart_detail
# from .forms import CartAddProductForm

# # Create your tests here.
# class CartAddViewTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         # Create test category
#         Category.objects.create(name="Test Category", slug="test-category")
#         self.product = Product.objects.create(category_id=1, name="Test Product",slug="test-product", price=10.00)
#         self.cart_session_id = settings.CART_SESSION_ID

#     def test_cart_initialization(self):
#         request = self.factory.get("/")
#         cart = Cart(request)
#         self.assertEqual(cart.cart, {})
