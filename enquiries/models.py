from django.db import models
from puppies.models import Puppy

# Model to store customer enquiries and contact form submissions
class Enquiry(models.Model):
    # Customer contact details
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    # Optional link to a specific puppy they are interested in
    puppy = models.ForeignKey(Puppy, on_delete=models.SET_NULL, null=True, blank=True)

    # Message or questions from the customer
    message = models.TextField()

    # Admin tracking: whether the customer has been contacted back
    is_contacted = models.BooleanField(default=False)

    # Date and time the enquiry was submitted
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.puppy:
            return f"Enquiry from {self.name} about {self.puppy.name}"
        return f"General Enquiry from {self.name}"

    class Meta:
        verbose_name_plural = "Enquiries"
