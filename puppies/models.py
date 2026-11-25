import urllib.parse
from django.db import models

# Model representing a Teacup Puppy available for adoption at TeddyPups
class Puppy(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Male & Female', 'Male & Female'),
    ]

    # Name of the puppy (e.g. "Max", "Chloe", "Coco")
    name = models.CharField(max_length=100)

    # Breed (e.g. "Teacup Maltipoo", "Korean Teacup Poodle", "Toy Poodle")
    breed = models.CharField(max_length=100)

    # Age (e.g. "3 months", "2 months")
    age = models.CharField(max_length=50)

    # Gender (Male, Female, or Male & Female)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Male')

    # Price in AED (e.g. 12000 AED)
    price = models.IntegerField(default=0)

    # Description (temperament, personality, origin)
    description = models.TextField()

    # Puppy photo
    image = models.ImageField(upload_to='puppies/', blank=True, null=True)

    # Health status
    is_vaccinated = models.BooleanField(default=True)

    # Availability: True = Available in Dubai, False = Already Gone Home
    is_available = models.BooleanField(default=True)

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.breed}"

    # Generates exact WhatsApp click-to-chat URL matching reference site
    def get_whatsapp_url(self):
        phone_number = "919898124987"  # Exact WhatsApp from reference site
        message = f"Hi TeddyPups, I'd like to ask about {self.name} ({self.breed}). Is {self.name} still available?"
        encoded_message = urllib.parse.quote(message)
        return f"https://wa.me/{phone_number}?text={encoded_message}"

    class Meta:
        verbose_name_plural = "Puppies"
