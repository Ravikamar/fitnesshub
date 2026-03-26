import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitnesshub_project.settings')
django.setup()

from gym.models import MembershipPlan
from shop.models import Category, Product

def populate():
    # Membership Plans
    plans = [
        {
            'name': 'Basic',
            'description': 'Perfect for beginners looking to start their fitness journey.',
            'price': 29.99,
            'duration_months': 1,
            'features': 'Gym Access, Basic Equipment, Locker Room'
        },
        {
            'name': 'Pro',
            'description': 'Advanced features for serious athletes and gym enthusiasts.',
            'price': 49.99,
            'duration_months': 1,
            'features': 'Gym Access, All Equipment, Group Classes, 1 PT Session'
        },
        {
            'name': 'Elite',
            'description': 'The ultimate gym experience with all-inclusive benefits.',
            'price': 89.99,
            'duration_months': 1,
            'features': 'Gym Access, All Equipment, Unlimited Classes, 4 PT Sessions, Sauna access'
        }
    ]

    for p in plans:
        MembershipPlan.objects.get_or_create(**p)

    # Categories
    supplements, _ = Category.objects.get_or_create(name='Supplements', slug='supplements')
    equipment, _ = Category.objects.get_or_create(name='Exercise Equipment', slug='exercise-equipment')

    # Products
    products = [
        {
            'category': supplements,
            'name': 'Whey Protein Isolation',
            'slug': 'whey-protein-isolation',
            'description': 'High-quality protein for muscle recovery and growth.',
            'price': 55.00,
            'stock': 50
        },
        {
            'category': supplements,
            'name': 'Pre-Workout Energizer',
            'slug': 'pre-workout-energizer',
            'description': 'Boost your energy and focus before every workout.',
            'price': 35.00,
            'stock': 30
        },
        {
            'category': equipment,
            'name': 'Dumbbell Set (20kg)',
            'slug': 'dumbbell-set-20kg',
            'description': 'Adjustable dumbbell set for home or gym use.',
            'price': 120.00,
            'stock': 15
        },
        {
            'category': equipment,
            'name': 'Yoga Mat',
            'slug': 'yoga-mat',
            'description': 'Durable and non-slip mat for yoga and floor exercises.',
            'price': 25.00,
            'stock': 100
        }
    ]

    for prod in products:
        Product.objects.get_or_create(**prod)

    print("Sample data populated successfully!")

if __name__ == '__main__':
    populate()
