from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path('trending/', views.TrendingView.as_view(), name='trending'),
    path('section/<str:pk>/', views.SectionView.as_view(), name='section'),
    path('item/<str:pk>/', views.ItemView.as_view(), name='item'),
]