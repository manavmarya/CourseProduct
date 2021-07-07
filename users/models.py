from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from coursePortal.settings import AUTH_USER_MODEL


class UserManager(BaseUserManager):
    '''create different user type for future features'''
    def create_user(self, email, is_staff, is_superuser, is_active, password, name):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = True,
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, is_staff, is_superuser, password, name):
        '''staff profile'''
        user = self.create_user(
            email,
            password=password,
            name=name,
            is_staff=is_staff,
            is_superuser=False,
            is_active=True,
            
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, True, True, True, password, **kwargs)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="Email Address", max_length=255, unique=True) #email as unique
    is_staff = models.BooleanField(default=False) #defaul profile is non-staff
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    def __str__(self):
        return "{0}".format(self.name)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_courses(self):
        return self.course_set.all()
