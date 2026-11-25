from django.test import TestCase
from django.urls import reverse
from puppies.models import Puppy
from .models import Enquiry
from .forms import EnquiryForm

# Tests for Enquiries app (Models, Forms, and Views)
class EnquiryTest(TestCase):

    def setUp(self):
        # Create a sample puppy for testing enquiries
        self.puppy = Puppy.objects.create(
            name="Max",
            breed="Teacup Maltipoo",
            age="3 months",
            gender="Male",
            price=14000,
            description="Sweet teacup puppy in Dubai.",
            is_vaccinated=True,
            is_available=True
        )

    # 1. Test Enquiry model creation and string representation
    def test_enquiry_str(self):
        enquiry = Enquiry.objects.create(
            name="Fatima Al Mansoori",
            email="fatima@example.com",
            phone="+971 50 123 4567",
            puppy=self.puppy,
            message="Interested in visiting Max in Downtown Dubai."
        )
        self.assertIn("Fatima Al Mansoori", str(enquiry))
        self.assertIn("Max", str(enquiry))

    # 2. Test EnquiryForm validation with valid data
    def test_enquiry_form_valid(self):
        form = EnquiryForm(data={
            'name': 'Alexander Wright',
            'email': 'alex@example.com',
            'phone': '+971 55 987 6543',
            'puppy': self.puppy.id,
            'message': 'Can I schedule a viewing this Friday?'
        })
        self.assertTrue(form.is_valid())

    # 3. Test EnquiryForm validation fails when required fields are missing
    def test_enquiry_form_invalid(self):
        form = EnquiryForm(data={
            'name': '',
            'email': 'not-an-email',
            'phone': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('email', form.errors)

    # 4. Test GET contact page
    def test_contact_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertContains(response, 'Downtown Dubai')

    # 5. Test POST enquiry submission
    def test_contact_post_submission(self):
        response = self.client.post(reverse('contact'), {
            'name': 'Sarah Jenkins',
            'email': 'sarah@example.com',
            'phone': '+971 52 333 4444',
            'puppy': self.puppy.id,
            'message': 'I would love to adopt Max!'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Enquiry.objects.count(), 1)
        enquiry = Enquiry.objects.first()
        self.assertEqual(enquiry.name, 'Sarah Jenkins')
        self.assertEqual(enquiry.puppy, self.puppy)
        self.assertContains(response, 'Thank you! Your enquiry has been received')
