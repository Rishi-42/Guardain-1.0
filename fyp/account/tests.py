from urllib import response
from django.test import TestCase
from selenium import webdriver
from .forms import RegistrationForm
class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'dashboardpharmacy.html')

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_register_form(self):
        form = RegistrationForm(data={'first_name': 'test', 'last_name': 'test', 'email': 'test@gmail.com', 'password': 'testtest','confirm_password': 'testtest', 'term':'True','user_type': 'pharmacist'})
        self.assertTrue(form.is_valid())
