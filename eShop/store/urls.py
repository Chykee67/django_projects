from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path('trending/', views.TrendingView.as_view(), name='trending'),
    path('section/<str:pk>/', views.SectionView.as_view(), name='section'),
    path('item/<item_description>/', views.ItemView.as_view(), name='item'),
    path('add_to_cart/<item_description>/', views.AddToCartView.as_view(), name='add_to_cart'),
]