from django.test import TestCase
from selenium import webdriver

class SystemTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def test_system(self):
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


text = "hello world, hola, test 2, test3"
x = text.split(',')
print(x)
]