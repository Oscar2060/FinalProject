from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Account, User

class TestAppUrls(SimpleTestCase):

    def test_url_name(self):  
        response = self.client.get('final_app/cars')
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('home_page'))
        self.assertTemplateUsed(response, "final_app/homepage.html")

class AccountTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User
        cls.account = Account.objects.create(user=user, name='name', city='aldk', bio='asdflj')

    def test_content(self):
        self.assertEqual(self.account.name, 'name')