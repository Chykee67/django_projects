from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path("", views.ReviewsIndexView.as_view(), name="index"),
    path("add_product_review/<item_description>/", views.AddProductReviewView.as_view(), name="add_product_review"),
]