from django.db import models

from login.models import User


class ProductReviewsQuerySet(models.QuerySet):
    
    def product_reviews(self):
        return self.filter(category="product_review")

class ProductReviewsManager(models.Manager):

    def get_queryset(self):
        return ProductReviewsQuerySet(self.model, using=_db)

    def product_reviews(self):
        return self.get_queryset().product_reviews()

class SiteReviewsQuerySet(models.QuerySet):
    
    def site_reviews(self):
        return self.filter(category="site_review")

class SiteReviewsManager(models.Manager):

    def get_queryset(self):
        return SiteReviewsQuerySet(self.model, using=_db)

    def site_reviews(self):
        return self.get_queryset().site_reviews()

class SuggestionsQuerySet(models.QuerySet):
    
    def suggestions(self):
        self.filter(category="suggestion")

class SuggestionsManager(models.Manager):

    def get_queryset(self):
        return SuggestionsQuerySet(self.model, using=_db)

    def suggestions(self):
        return self.get_queryset().suggestions()


class Feedback(models.Model):

    def get_category():
        return {
            "product_review": "product_review",
            "site_review": "site_review",
            "suggestion": "suggestion",
        }

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    category = models.CharField(
        max_length=40,
        choices=get_category,
    )

    review = models.TextField(
        max_length=300,
    )

    feedbacks = models.Manager()

    product_reviews = ProductReviewsManager()
    site_reviews = SiteReviewsManager()
    suggestions = SuggestionsManager()

    def __str__(self):
        return self.review

