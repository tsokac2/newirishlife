from django.test import TestCase


class TestViews(TestCase):
    def test_shoping_bag_page(self):
        """ Test shoping bag page renders correct page """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'bag/bag.html')
