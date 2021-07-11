from django.test import TestCase
from .forms import OrderForm


class TestViews(TestCase):
    def test_checkout_page_redirects_when_logged_out(self):
        """ Test Checkout redirects when user is logged out """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)
