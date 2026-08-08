from django.core.management.base import BaseCommand
from store.models import Category, Product


PRODUCTS = [
    {
        "name": "iPhone 16 Pro",
        "price": 129999,
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=900",
        "description": "Latest Apple flagship smartphone.",
    },
    {
        "name": "Sony Headphones",
        "price": 5999,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=900",
        "description": "Premium noise cancelling headphones.",
    },
    {
        "name": "Nike Air Max",
        "price": 3999,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=900",
        "description": "Comfortable and stylish running shoes.",
    },
    {
        "name": "Smart Watch",
        "price": 2499,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=900",
        "description": "Track fitness and notifications.",
    },
    {
        "name": "Laptop",
        "price": 65999,
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=900",
        "description": "High performance laptop for work and study.",
    },
    {
        "name": "Gaming Mouse",
        "price": 1499,
        "image": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=900",
        "description": "Precision RGB gaming mouse.",
    },
    {
        "name": "Samsung Galaxy S25",
        "price": 79999,
        "image": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=900",
        "description": "Powerful smartphone with premium design.",
    },
    {
        "name": "Canon Camera",
        "price": 54999,
        "image": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=900",
        "description": "Professional camera for stunning photography.",
    },
    {
        "name": "Leather Backpack",
        "price": 2999,
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=900",
        "description": "Stylish and durable everyday backpack.",
    },
    {
        "name": "Premium Sunglasses",
        "price": 1999,
        "image": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=900",
        "description": "Stylish sunglasses with premium finish.",
    },
    {
        "name": "Mechanical Keyboard",
        "price": 3499,
        "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=900",
        "description": "Premium mechanical keyboard for gaming.",
    },
    {
        "name": "Premium Perfume",
        "price": 2499,
        "image": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=900",
        "description": "Elegant fragrance for a premium experience.",
    },
]


class Command(BaseCommand):

    help = "Create default ShopEase products"

    def handle(self, *args, **kwargs):

        category, created = Category.objects.get_or_create(
            name="ShopEase Products"
        )

        for item in PRODUCTS:

            product, created = Product.objects.get_or_create(
                name=item["name"],
                defaults={
                    "category": category,
                    "description": item["description"],
                    "price": item["price"],
                    "image_url": item["image"],
                    "stock": 100,
                }
            )

            if not created:
                product.category = category
                product.description = item["description"]
                product.price = item["price"]
                product.image_url = item["image"]
                product.stock = 100
                product.save()

        self.stdout.write(
            self.style.SUCCESS(
                "ShopEase products created successfully!"
            )
        )