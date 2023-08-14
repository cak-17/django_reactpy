from django.test import TestCase
from api.models import Product


class ProductTestCase(TestCase):
  def testProduct(self):
    product = Product(
      name="Test1",
      description="This is a test",
      price=5.0
    )
    self.assertEqual(product.name, "Test1")
    self.assertEqual(product.description, "This is a test")
    self.assertEqual(product.price, 5.0)
