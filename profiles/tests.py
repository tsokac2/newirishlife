from django.test import TestCase
from .forms import UserProfileForm


class TestViews(TestCase):
    def test_user_profile_page(self):
        """ Test User Profile redirects when user is logged out """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)


class TestUserForm(TestCase):
    """ Test to test that form field is valid """
    def test_edit_profile_form(self):
        form = UserProfileForm(
            {
                'full_name': 'John Snow',
                'phone_number': '+38508555566655',
                'city': 'Winterfell'
                })
        self.assertTrue(form.is_valid())
