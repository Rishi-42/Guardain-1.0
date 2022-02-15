from urllib import response
from django.test import TestCase
from selenium import webdriver
from account.forms import RegistrationForm

# class FunctionalTestCase(TestCase):
#     def setUp(self):
#         self.browser = webdriver.Firefox()

#     def test(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('Order ID', self.browser.page_source)
#         # assert 'Pharmacy' in browser.page_source
#         # assert browser.page_source.find('Pharmacy')

#     def tearDown(self):
#         self.browser.quit()

# class UnitTestCase(TestCase):

#     def test_home_homepage_template(self):
#         response = self.client.get('/')
#         self.assertTemplateUsed(response, 'dashboardpharmacy.html')

#     def test_home_status_code(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
    
#     def test_register_form(self):
#         form = RegistrationForm(data={'first_name': 'test', 'last_name': 'test', 'email': 'test@gmail.com', 'password': 'test','confirm_password': 'test', 'term':'True','user_type': 'pharmacist'})
#         self.assertTrue(form.is_valid())

