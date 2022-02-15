from urllib import response
from django.test import TestCase
from selenium import webdriver
from .forms import RegistrationForm
from .models import Account, Type_user
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

    def test_account_object(self):
        user = Account.objects.create_user(
            first_name = 'test',
            last_name = 'test',
            username = 'test',
            email = 'test@gmail.com',
            password = 'testtest',
            user_type = 'pharmacist'
        )
        user.save()
        # pulled_user = Account.objects.get(id=1)
        pulled_user = Account.objects.get(email='test@gmail.com')
        self.assertEqual(user.first_name, pulled_user.first_name)
        self.assertEqual(user.last_name, pulled_user.last_name)
        self.assertEqual(user.username, pulled_user.username)
        self.assertEqual(user.email, pulled_user.email)
        self.assertEqual(user.password, pulled_user.password)
        self.assertEqual(user.user_type, pulled_user.user_type)

    def test_account_object_counsellor(self):
        # user = Account.objects.create_user(
        #     first_name = 'test',
        #     last_name = 'test',
        #     username = 'test',
        #     email = 'test@gmail.com',
        #     password = 'testtest',
        #     user_type = 'counsellor'
        # )
        # user.save()
        # pulled_user = Account.objects.get(id=1)
        # print(pulled_user.user_type)
        user_type_pull = Type_user.objects.get(id=1)
        self.assertEquals(user_type_pull.is_counsellor, True)

