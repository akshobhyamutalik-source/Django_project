from django.db import migrations
from django.contrib.auth.hashers import make_password

def seed_puppies_and_admin(apps, schema_editor):
    Puppy = apps.get_model('puppies', 'Puppy')

    puppies_data = [
        {
            'name': 'Max',
            'breed': 'Teacup Maltipoo',
            'age': '3 months',
            'gender': 'Male',
            'price': 14000,
            'description': 'Max is a premium Teacup Maltipoo with a soft curly coat and button nose. Calm, loving, and ready to meet you at our Downtown Dubai showroom.',
            'image': 'puppies/bella.jpg',
            'is_vaccinated': True,
            'is_available': True,
        },
        {
            'name': 'Chloe',
            'breed': 'Korean Teacup Poodle',
            'age': '2 months',
            'gender': 'Female',
            'price': 15500,
            'description': 'Chloe is an exquisite Korean Teacup Poodle with apricot curls and micro muzzle. Hypoallergenic, playful, and comes with full international health passport.',
            'image': 'puppies/coco.jpg',
            'is_vaccinated': True,
            'is_available': True,
        },
        {
            'name': 'Coco',
            'breed': 'Korean Teacup Pomeranian',
            'age': '2.5 months',
            'gender': 'Female',
            'price': 13000,
            'description': 'Coco is a gorgeous cream teacup Pomeranian with thick plush fur and compact posture. Super affectionate and gentle with children.',
            'image': 'puppies/daisy.jpg',
            'is_vaccinated': True,
            'is_available': True,
        },
        {
            'name': 'Oliver & Daisy',
            'breed': 'Toy Poodle',
            'age': '2 months',
            'gender': 'Male & Female',
            'price': 12000,
            'description': 'Beautiful red Toy Poodles with champion bloodlines. Both puppies are fully dewormed, vet-certified, and microchipped.',
            'image': 'puppies/rocky.jpg',
            'is_vaccinated': True,
            'is_available': True,
        },
        {
            'name': 'Leo',
            'breed': 'Teacup Cavapoo',
            'age': '3 months',
            'gender': 'Male',
            'price': 13500,
            'description': 'Leo is a sweet, fluffy ruby Cavapoo with loving dark eyes and wonderful social temperament. Ready for same-day adoption.',
            'image': 'puppies/leo.jpg',
            'is_vaccinated': True,
            'is_available': True,
        },
        {
            'name': 'Cooper',
            'breed': 'Imperial Shih Tzu',
            'age': '2 months',
            'gender': 'Male',
            'price': 11000,
            'description': 'Adopted by a lovely family in Dubai Marina. Cooper is flourishing in his new home.',
            'image': 'puppies/milo.jpg',
            'is_vaccinated': True,
            'is_available': False,
        },
        {
            'name': 'Bella',
            'breed': 'Teacup Maltipoo',
            'age': '3 months',
            'gender': 'Female',
            'price': 14000,
            'description': 'Adopted by a warm family residing on Palm Jumeirah.',
            'image': 'puppies/bella.jpg',
            'is_vaccinated': True,
            'is_available': False,
        },
    ]

    for p in puppies_data:
        Puppy.objects.get_or_create(
            name=p['name'],
            breed=p['breed'],
            defaults=p
        )

    # Seed default admin user for Render live demo if not existing
    try:
        User = apps.get_model('auth', 'User')
        if not User.objects.filter(username='admin').exists():
            User.objects.create(
                username='admin',
                email='admin@teddypups.ae',
                password=make_password('admin123'),
                is_staff=True,
                is_superuser=True,
                is_active=True,
            )
    except Exception:
        pass

def reverse_seed(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('puppies', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_puppies_and_admin, reverse_code=reverse_seed),
    ]
