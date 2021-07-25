from django.test import TestCase


class TestViews(TestCase):
    def test_trip_page(self):
        """ Test Trip page renders correct page """
        response = self.client.get('/trip')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'trip/trip.html')

