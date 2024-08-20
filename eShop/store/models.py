from django.db import models


class Category(models.Model):

    """ Class defining Categories of items """

    description = models.CharField(
        max_length=32,
        )

class Subcategory(models.Model):

    """ Class defining subcategories of objects """

    description = models.CharField(
        max_length=32,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )


class Item(models.Model):

    """ Class that defines item objects """

    description = models.CharField(
        max_length = 32,
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    price = models.IntegerField() #Use MinValueValidator here

    quantity = models.IntegerField()



# Create your models here.
