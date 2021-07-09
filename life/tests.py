from django.test import TestCase

class TestViews(TestCase):
    def test_life_page(self):
        """ Test Life page renders correct page """
        response = self.client.get('/life')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'life/life.html')
