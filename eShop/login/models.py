from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    user_email = models.EmailField(max_length=254)
    about_user = models.TextField(
        max_length=300,
        blank=True,
    )
    country_of_residence = models.CharField(
        max_length=100,
        blank=True,
        )
    state_of_residence = models.CharField(
        max_length=100,
        blank=True,
        )
    city_of_residence = models.CharField(
        max_length=100,
        blank=True,
        )
    street_address = models.TextField(
        max_length=300,
        blank=True,
        )

    def __str__(self):
        return self.user_name

class Cart(models.Model):
    ...
    #try to use generatedfield from django.models here to calculate the total worth of items in the cart

class Section(models.Model):
    ...

class Item(models.Model):
    ...
# Create your models here.
