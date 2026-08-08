from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Wishlist, Cart

# ADD / REMOVE WISHLIST
def toggle_wishlist(request, pk):
    product = get_object_or_404(Product, id=pk)

    item = Wishlist.objects.filter(user=request.user, product=product)

    if item.exists():
        item.delete()
        return JsonResponse({"status": "removed"})
    else:
        Wishlist.objects.create(user=request.user, product=product)
        return JsonResponse({"status": "added"})


# WISHLIST PAGE
def wishlist_page(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, "wishlist.html", {"items": items})


# ADD TO CART
def add_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse({"status": "added"})


# CART PAGE
def cart_page(request):
    items = Cart.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in items)

    return render(request, "cart.html", {"items": items, "total": total})