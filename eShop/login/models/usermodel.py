from datetime import date

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group, Permission


class UserManager(BaseUserManager):

    """ Manager for User model below """

    def create_user(self, email, date_of_birth, first_name, last_name, password=None,):

        #creates and saves user to database.
        #takes username_field, password and required fields as args.

        if not email:
            raise ValueError("User must have an email address!")

        user = self.model(
            email=self.normalize_email(email), date_of_birth=date_of_birth, first_name=first_name, last_name=last_name,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, email, date_of_birth, first_name, last_name, password,):

        #creates and saves a superuser to database.
        #takes same arguments as create_user, but sets is_admin to True.

        user = self.create_user(
            email=email, date_of_birth=date_of_birth, first_name=first_name, last_name=last_name, password=password,
            )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    first_name = models.CharField(
        max_length = 40,
        default="first name",
    )

    last_name = models.CharField(
        max_length=40,
        default="last name",
    )

    email = models.EmailField(
        max_length=40,
        unique=True,
        verbose_name = "email address",
        default="useremail@mail.com",
    )

    date_of_birth = models.DateField(default=date.today)

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

    groups = models.ManyToManyField(Group)

    permissions = models.ManyToManyField(Permission)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    users = UserManager()

    profile_photo = models.ImageField(
        upload_to="profile_photos/",
        blank=True,
    )

    USERNAME_FIELD = "email"

    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = [
        "date_of_birth",
        "first_name",
        "last_name",
        ]


    def get_full_name():
        return f"{self.first_name} {self.last_name}"

    def get_short_name():
        return f"{self.first_name}"

    def __str__(self):
        if self.first_name:
            return self.first_name
        else:
            return self.email
    
    def has_perm(self, perm, obj=None):

        #Check if user has a certain permission

        return True

    def has_module_perms(self, app_label):
        
        #Does the user have the permission to view the app with app_label arg

        return True

    def get_shipping_address(self):
        if self.street_address and self.city_of_residence:
            return f"""
            {self.street_address.rstrip(',')},
            {self.city_of_residence.rstrip(',')},
            {self.state_of_residence.rstrip(',')},
            {self.country_of_residence.rstrip(',')}.
            """
        else:
            return False

    @property
    def is_staff(self):

        #Is the user a member of staff?

        return self.is_admin
