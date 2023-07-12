from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import datetime
from .manager import MyUserManager
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.TextField(max_length=255, default=None, null=True)
    last_name = models.TextField(max_length=255, default=None, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    my_country = models.TextField(max_length=255, default=None, null=True)
    fav_countries = models.JSONField(null=True)
    creation_date = models.DateTimeField(default=datetime.date.today())
    update_date = models.DateField(default=datetime.date.today())
    last_request = models.DateField(default=datetime.date.today())

    objects = MyUserManager() 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin