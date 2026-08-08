from django.core.management.base import BaseCommand
from store.models import Product, Category


class Command(BaseCommand):

    help = "Add ShopEase products with images"

    def handle(self, *args, **kwargs):

        category, created = Category.objects.get_or_create(
            name="ShopEase Products"
        )

        products = [

            {
                "name": "iPhone 16 Pro",
                "price": 129999,
                "description": "Premium Apple smartphone with advanced camera and powerful performance.",
                "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=1000",
                "stock": 50,
            },

            {
                "name": "Samsung Galaxy S25",
                "price": 79999,
                "description": "Premium smartphone with modern design and powerful performance.",
                "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=1000",
                "stock": 50,
            },

            {
                "name": "MacBook Air M4",
                "price": 114999,
                "description": "Slim and powerful laptop for work, study and creativity.",
                "image_url": "https://images.unsplash.com/photo-1517336714739-489689fd1ca8?w=1000",
                "stock": 30,
            },

            {
                "name": "Dell XPS 15",
                "price": 109999,
                "description": "Professional laptop with premium display and modern design.",
                "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=1000",
                "stock": 30,
            },

            {
                "name": "Sony WH-1000XM5",
                "price": 29999,
                "description": "Premium wireless headphones with immersive sound.",
                "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=1000",
                "stock": 40,
            },

            {
                "name": "Apple Watch Series 10",
                "price": 46999,
                "description": "Smart wearable with fitness tracking and notifications.",
                "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=1000",
                "stock": 35,
            },

            {
                "name": "Nike Air Max",
                "price": 8999,
                "description": "Comfortable premium sneakers for everyday lifestyle.",
                "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=1000",
                "stock": 60,
            },

            {
                "name": "Adidas Ultraboost",
                "price": 11999,
                "description": "Modern running shoes offering comfort and support.",
                "image_url": "https://images.unsplash.com/photo-1552346154-21d32810aba3?w=1000",
                "stock": 45,
            },

            {
                "name": "Canon EOS Camera",
                "price": 74999,
                "description": "Professional camera for photography and content creation.",
                "image_url": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=1000",
                "stock": 20,
            },

            {
                "name": "Logitech MX Master Mouse",
                "price": 8999,
                "description": "Premium wireless mouse designed for productivity.",
                "image_url": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=1000",
                "stock": 50,
            },

            {
                "name": "Mechanical Keyboard",
                "price": 5999,
                "description": "Premium mechanical keyboard for gaming and productivity.",
                "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=1000",
                "stock": 50,
            },

            {
                "name": "JBL Bluetooth Speaker",
                "price": 6999,
                "description": "Portable Bluetooth speaker with powerful sound.",
                "image_url": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=1000",
                "stock": 40,
            },

        ]

        for data in products:

            product, created = Product.objects.update_or_create(

                name=data["name"],

                defaults={
                    "category": category,
                    "description": data["description"],
                    "price": data["price"],
                    "image_url": data["image_url"],
                    "stock": data["stock"],
                }
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Added: {product.name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Updated: {product.name}"
                    )
                )

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "ALL PRODUCTS AND IMAGES UPDATED SUCCESSFULLY!"
            )
        )