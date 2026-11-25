from django.test import TestCase
from django.urls import reverse
from .models import Puppy

# Tests for Puppies app (Models and Views matching TeddyPups)
class PuppyModelAndViewsTest(TestCase):

    def setUp(self):
        # Create sample test puppies
        self.puppy1 = Puppy.objects.create(
            name="Max",
            breed="Teacup Maltipoo",
            age="3 months",
            gender="Male",
            price=14000,
            description="Playful and loving teacup puppy.",
            is_vaccinated=True,
            is_available=True
        )
        self.puppy2 = Puppy.objects.create(
            name="Cooper",
            breed="Imperial Shih Tzu",
            age="2 months",
            gender="Male",
            price=11000,
            description="Adopted puppy in Dubai.",
            is_vaccinated=True,
            is_available=False  # Already gone home
        )

    # 1. Test model string representation
    def test_puppy_str(self):
        self.assertEqual(str(self.puppy1), "Max - Teacup Maltipoo")

    # 2. Test WhatsApp URL generation
    def test_whatsapp_url(self):
        wa_url = self.puppy1.get_whatsapp_url()
        self.assertIn("https://wa.me/919898124987", wa_url)
        self.assertIn("Max", wa_url)

    # 3. Test puppies list view (shows available and gone home)
    def test_puppies_list_view(self):
        response = self.client.get(reverse('puppies'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'puppies.html')
        self.assertContains(response, "Max")
        self.assertContains(response, "Cooper")
        self.assertContains(response, "Already gone home")

    # 4. Test puppy details view for valid puppy ID
    def test_puppy_detail_valid(self):
        response = self.client.get(reverse('puppy_details', args=[self.puppy1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'puppy_details.html')
        self.assertContains(response, "Max")
        self.assertContains(response, "Teacup Maltipoo")

    # 5. Test puppy details view for invalid puppy ID (returns 404)
    def test_puppy_detail_invalid(self):
        response = self.client.get(reverse('puppy_details', args=[9999]))
        self.assertEqual(response.status_code, 404)

    # 6. Test search filter by breed
    def test_puppy_search(self):
        response = self.client.get(reverse('puppies') + '?search=Maltipoo')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Max")
        self.assertNotContains(response, "Cooper")
