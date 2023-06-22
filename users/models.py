from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email is Required')
        if not password:
            raise ValueError('The Password is Required')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name,
                          last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(first_name, last_name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CustomerProfile(models.Model):
    avatar = models.ImageField(upload_to='profiles_img')
    phone = models.CharField(max_length=50, blank=False, unique=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Address(models.Model):
    country = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=100, blank=False)
    address_line1 = models.CharField(max_length=255, blank=False)
    address_line2 = models.CharField(max_length=255, blank=True)
    profile = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE,
                                related_name='user_addresses', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.country} {self.city}'
