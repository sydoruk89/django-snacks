from django.test import SimpleTestCase
from django.urls import reverse

class SnacksTests(SimpleTestCase):

    def test_home_page_status(self):
        self.helper_status_code_200('home')

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_status(self):
        self.helper_status_code_200('about')

    def helper_status_code_200(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)