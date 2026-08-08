from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Product, Wishlist


# ==========================================================
# PRODUCT IMAGES
# ==========================================================

IMAGE_URLS = {

    "iPhone 16 Pro":
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=900",

    "Sony Headphones":
        "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=900",

    "Nike Air Max":
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=900",

    "Smart Watch":
        "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=900",

    "Laptop":
        "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=900",

    "Gaming Mouse":
        "https://images.unsplash.com/photo-1527814050087-3793815479db?w=900",

    "Samsung Galaxy":
        "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=900",

    "Camera":
        "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=900",

    "Backpack":
        "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=900",

    "Sunglasses":
        "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=900",

    "Keyboard":
        "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=900",

    "Premium Perfume":
        "https://images.unsplash.com/photo-1541643600914-78b084683601?w=900",
}


# ==========================================================
# HOME
# ==========================================================

def home(request):

    products = Product.objects.all().order_by("id")

    unique_products = []
    seen_names = set()

    for product in products:

        product_name = product.name.strip()

        # Remove duplicate product names
        if product_name.lower() in seen_names:
            continue

        seen_names.add(product_name.lower())

        # Image priority

        if product.image:
            product.display_image = product.image.url

        elif product.image_url:
            product.display_image = product.image_url

        elif product_name in IMAGE_URLS:
            product.display_image = IMAGE_URLS[product_name]

        else:
            product.display_image = (
                "https://images.unsplash.com/"
                "photo-1523275335684-37898b6baf30?w=900"
            )

        unique_products.append(product)

    # Wishlist products for current user

    wishlist_ids = set()

    if request.user.is_authenticated:

        wishlist_ids = set(
            Wishlist.objects.filter(
                user=request.user
            ).values_list(
                "product_id",
                flat=True
            )
        )

    return render(
        request,
        "home.html",
        {
            "products": unique_products,
            "wishlist_ids": wishlist_ids,
        }
    )


# ==========================================================
# PRODUCT DETAIL
# ==========================================================

def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    product_name = product.name.strip()

    if product.image:

        product.display_image = product.image.url

    elif product.image_url:

        product.display_image = product.image_url

    elif product_name in IMAGE_URLS:

        product.display_image = IMAGE_URLS[product_name]

    else:

        product.display_image = (
            "https://images.unsplash.com/"
            "photo-1523275335684-37898b6baf30?w=900"
        )

    return render(
        request,
        "product_detail.html",
        {
            "product": product
        }
    )


# ==========================================================
# WISHLIST PAGE
# ==========================================================

@login_required
def wishlist_view(request):

    wishlist = Wishlist.objects.filter(
        user=request.user
    ).select_related("product")

    for item in wishlist:

        product = item.product
        product_name = product.name.strip()

        if product.image:

            product.display_image = product.image.url

        elif product.image_url:

            product.display_image = product.image_url

        elif product_name in IMAGE_URLS:

            product.display_image = IMAGE_URLS[product_name]

        else:

            product.display_image = (
                "https://images.unsplash.com/"
                "photo-1523275335684-37898b6baf30?w=900"
            )

    return render(
        request,
        "wishlist.html",
        {
            "wishlist": wishlist
        }
    )


# ==========================================================
# ADD TO WISHLIST
# ==========================================================

@login_required
def add_to_wishlist(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect("wishlist")


# ==========================================================
# REMOVE FROM WISHLIST
# ==========================================================

@login_required
def remove_from_wishlist(request, wishlist_id):

    wishlist_item = get_object_or_404(
        Wishlist,
        id=wishlist_id,
        user=request.user
    )

    wishlist_item.delete()

    return redirect("wishlist")