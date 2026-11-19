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


# What each kind of user may do, written in code. A permission is named '<app>.<action>_<model>',
# the same names Django makes for every model (add_, change_, delete_, view_).
CUSTOMER_PERMISSIONS = {'product.view_product'}
SELLER_PERMISSIONS = {
    'product.view_product',
    'product.add_product',
    'product.change_product',
    'product.delete_product',
}


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

    # ---------- permissions ----------
    # Django asks these questions: the admin, PermissionRequiredMixin (has_perms) and the
    # {% if perms.product.add_product %} of the templates (has_perm, has_module_perms).
    # Without PermissionsMixin there are no groups or permission tables to look at, so the answers
    # come from the list at the top of this file: each kind of user has its own permissions.

    # the permissions of this user, a set of names like 'product.add_product'
    def get_permissions(self):
        if not self.is_active:
            return set()
        permissions = set()
        if self.is_customer:
            permissions |= CUSTOMER_PERMISSIONS
        if self.is_seller:
            permissions |= SELLER_PERMISSIONS
        return permissions

    # may this user do this action? a staff user can do everything
    def has_perm(self, perm, obj=None):
        return self.is_active and (self.is_staff or perm in self.get_permissions())

    # may this user do all of these actions? (PermissionRequiredMixin calls this one)
    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj) for perm in perm_list)

    # may this user see anything of this app? ('product.add_product' belongs to the app 'product')
    def has_module_perms(self, app_label):
        if not self.is_active:
            return False
        return self.is_staff or any(perm.split('.')[0] == app_label for perm in self.get_permissions())
