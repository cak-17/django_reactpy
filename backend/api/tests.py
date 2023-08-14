from django.test import TestCase
from api.models import Product
from api.serializers import ProductSerializer

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


class ProductSerializerTestCase(TestCase):
 def testProductSerializer(self):
   data =  {
      "name": "Pizza2",
      "description": "A testy pizza",
      "price": 42.0
   }
   product_serializer = ProductSerializer(data=data, partial=True)
   self.assertEqual(product_serializer.is_valid(), True)
