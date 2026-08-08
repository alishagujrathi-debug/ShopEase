from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/toggle/<int:pk>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('wishlist/', views.wishlist_page, name='wishlist_page'),

    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_page, name='cart_page'),
]