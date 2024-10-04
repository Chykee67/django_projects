from django.urls import path

from . import views

app_name = 'profile'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("orders/", views.OrdersTemplateView.as_view(), name='orders'),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("cart/remove_item/<item_description>/", views.RemoveItemView.as_view(), name="remove_from_cart"),
]