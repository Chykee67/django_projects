from django.urls import path

from . import views

app_name = 'profile'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("edit_profile/", views.EditProfileDataView.as_view(), name="edit_profile"),
    path("orders/", views.OrdersTemplateView.as_view(), name='orders'),
    path("orders/order_details/<int:order_id>/", views.OrderDetailView.as_view(), name='order_details'),
    path("orders/<orders_list>/", views.OrdersListView.as_view(), name='orders_list'),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("cart/remove_item/<item_description>/", views.RemoveItemView.as_view(), name="remove_from_cart"),
    path("confirm_order/<item_description>/", views.ConfirmOrderView.as_view(), name="confirm_order"),
    path("upload_profile_photo/", views.UploadProfilePhotoView.as_view(), name="upload_profile_photo")
]