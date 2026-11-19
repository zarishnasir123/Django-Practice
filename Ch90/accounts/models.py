from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

# Create your models here.

# The manager is the class that makes users (CustomUser.objects). Django's createsuperuser command
# calls create_superuser(), so a custom user model must have these two methods.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)        # makes the part after @ lowercase
        user = self.model(email=email, **extra_fields)
        user.set_password(password)                # saves the password hashed, never as plain text
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)  # is_staff = can enter /admin/
        return self.create_user(email, password, **extra_fields)

    # The login finds the user with this method. iexact = capital letters do not matter,
    # so the email can be typed in any case on the login page.
    def get_by_natural_key(self, email):
        return self.get(email__iexact=email)


# AbstractBaseUser gives only the password and last_login. Everything else is written here,
# so the user is built exactly as the project needs: the email is the login, and two flags tell
# the kind of user. There is no PermissionsMixin, so has_perm() and has_module_perms() are written below.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)   # the name shown on the site

    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)    # False = can not log in
    is_staff = models.BooleanField(default=False)    # True = can enter /admin/ and do everything there
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'         # the field used to log in
    REQUIRED_FIELDS = ['username']   # asked by createsuperuser (the email and password are always asked)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    # The admin asks these two questions before it shows anything.
    # has_perm: may this user do this action (add, change, delete, view a model)?
    # has_module_perms: may this user see this app (accounts, customer...) in the admin?
    # Without PermissionsMixin there are no groups or permissions to look at, so the answer
    # is simple: a staff user can do everything, any other user nothing.
    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
