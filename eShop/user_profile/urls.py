from django.urls import path

from . import views

app_name = 'profile'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("orders/", views.OrdersTemplateView.as_view(), name='orders'),
    path("orders/<orders_list>/", views.OrdersListView.as_view(), name='orders_list'),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("cart/remove_item/<item_description>/", views.RemoveItemView.as_view(), name="remove_from_cart"),
    path("confirm_order/<item_description>/", views.ConfirmOrderView.as_view(), name="confirm_order"),
]