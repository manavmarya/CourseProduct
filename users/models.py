from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import Group
from coursePortal.settings import AUTH_USER_MODEL


class UserManager(BaseUserManager):
    def create_user(self, email, is_staff, is_superuser, password, name):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, is_staff, is_superuser, password, nameUser):
        user = self.create_user(
            email,
            password=password,
            name=name,
            is_staff=is_staff,
            
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, True, True, password, **kwargs)
        user.save(using=self._db)
        return user

minmax_error = "Class not valid"

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="Email Address", max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()
    def __str__(self):
        return "{0}".format(self.name)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_absolute_url(self):
        return "/users/{0}/".format(self.pk)

    def get_courses(self):
        return self.course_set.all()
