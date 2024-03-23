from django.test import TestCase

# Create your tests here.
from .models import Product

class ProductTestCase(TestCase):
    """Test case for Product model."""
    def setUp(self):
        self.product = Product.objects.create(product_name="product test name", 
                                      product_description="product test description", 
                                      product_quantity=10, 
                                      product_expiration_date="2021-12-31"
                                      )
        

    def test_product(self):
        """Product quantity will be type int and greater than 0."""
        self.assertGreater(self.product.product_quantity, 0)
        self.assertIsInstance(self.product.product_quantity, int)
