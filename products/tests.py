from django.test import TestCase
from .models import Product


class TestViews(TestCase):

    def test_products_page(self):
        """ Test Products page renders correct page """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'products/products.html')


