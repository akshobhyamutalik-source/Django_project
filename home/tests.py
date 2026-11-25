from django.test import TestCase
from django.urls import reverse

# Tests for TeddyPups home and informational pages
class HomeViewsTest(TestCase):
    # Test that the home page loads successfully
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'TeddyPups')
        self.assertContains(response, 'Premium teacup')

    # Test that happy families page loads successfully
    def test_happy_families_page(self):
        response = self.client.get(reverse('happy_families'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'happy_families.html')
        self.assertContains(response, 'Happy families')

    # Test that how it works page loads successfully
    def test_how_it_works_page(self):
        response = self.client.get(reverse('how_it_works'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'how_it_works.html')
        self.assertContains(response, 'How it works')

    # Test that the FAQ page loads successfully
    def test_faq_page(self):
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq.html')
        self.assertContains(response, 'Questions & answers')
