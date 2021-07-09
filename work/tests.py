from django.test import TestCase

class TestViews(TestCase):
    def test_work_page(self):
        """ Test Work page renders correct page """
        response = self.client.get('/work')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'work/work.html')
