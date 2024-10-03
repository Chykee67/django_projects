from django.urls import path

from . import views

app_name = 'profile'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("orders/", views.OrdersTemplateView.as_view(), name='orders'),
]