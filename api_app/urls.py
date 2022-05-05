from django.urls import path
from .views import CartItemView


urlpatterns = [
    path('cart-item/', CartItemView.as_view()),
    path('cart-item/<int:id>', CartItemView.as_view()),
    path('cart-item/<int:id>/change', CartItemView.as_view()),
    path('cart-item/<int:id>/delete', CartItemView.as_view()),
]
