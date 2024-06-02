from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import about, index

class TestUrls(SimpleTestCase):
    def test_main(self):
        url = reverse('mainPage')
        self.assertEqual(resolve(url).func, index)

    def test_about(self):
        url = reverse('aboutPage')
        self.assertEqual(resolve(url).func, about)

# python manage.py test main
