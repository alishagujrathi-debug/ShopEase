from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import CartItem
from store.models import Product, Category


# =========================================================
# SHOP PRODUCTS
# =========================================================

SHOP_PRODUCTS = [

    {
        "id": 1,
        "name": "iPhone 16 Pro",
        "price": 129999,
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800",
        "description": "Latest Apple flagship smartphone."
    },

    {
        "id": 2,
        "name": "Sony Headphones",
        "price": 5999,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800",
        "description": "Premium noise cancelling headphones."
    },

    {
        "id": 3,
        "name": "Nike Air Max",
        "price": 3999,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800",
        "description": "Comfortable and stylish running shoes."
    },

    {
        "id": 4,
        "name": "Smart Watch",
        "price": 2499,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800",
        "description": "Track fitness and notifications."
    },

    {
        "id": 5,
        "name": "Laptop",
        "price": 65999,
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800",
        "description": "High performance laptop."
    },

    {
        "id": 6,
        "name": "Gaming Mouse",
        "price": 1499,
        "image": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=800",
        "description": "RGB gaming mouse."
    },

]


# =========================================================
# CART VIEW
# =========================================================

@login_required
def cart_view(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    ).select_related("product")

    total = sum(
        item.total_price()
        for item in cart_items
    )

    return render(
        request,
        "cart.html",
        {
            "cart_items": cart_items,
            "total": total,
        }
    )


# =========================================================
# ADD TO CART
# =========================================================

@login_required
def add_to_cart(request, product_id):

    product_data = next(
        (
            product
            for product in SHOP_PRODUCTS
            if product["id"] == product_id
        ),
        None
    )

    if product_data is None:
        return redirect("home")


    # Create category

    category, created = Category.objects.get_or_create(
        name="ShopEase Products"
    )


    # Find product

    product = Product.objects.filter(
        name=product_data["name"]
    ).first()


    # Create product if not available

    if product is None:

        product = Product.objects.create(

            category=category,

            name=product_data["name"],

            description=product_data["description"],

            price=product_data["price"],

            image_url=product_data["image"],

            stock=100

        )

    else:

        # Always keep online image URL updated

        product.image_url = product_data["image"]

        product.save()


    # Add to cart

    cart_item, created = CartItem.objects.get_or_create(

        user=request.user,

        product=product

    )


    # Increase quantity

    if not created:

        cart_item.quantity += 1

        cart_item.save()


    return redirect("cart")


# =========================================================
# REMOVE FROM CART
# =========================================================

@login_required
def remove_from_cart(request, product_id):

    cart_item = get_object_or_404(

        CartItem,

        product_id=product_id,

        user=request.user

    )

    cart_item.delete()

    return redirect("cart")


# =========================================================
# CHECKOUT
# =========================================================

@login_required
def checkout(request):

    cart_items = CartItem.objects.filter(

        user=request.user

    ).select_related("product")


    # Empty cart

    if not cart_items.exists():

        return redirect("cart")


    # Calculate total

    total = sum(

        item.total_price()

        for item in cart_items

    )


    # Form submitted

    if request.method == "POST":

        full_name = request.POST.get("full_name")

        address = request.POST.get("address")

        city = request.POST.get("city")

        pincode = request.POST.get("pincode")

        phone = request.POST.get("phone")


        return render(

            request,

            "order_success.html",

            {

                "full_name": full_name,

                "address": address,

                "city": city,

                "pincode": pincode,

                "phone": phone,

                "total": total,

            }

        )


    # Checkout page

    return render(

        request,

        "checkout.html",

        {

            "cart_items": cart_items,

            "total": total,

        }

    )