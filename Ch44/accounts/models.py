from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):    
    def create_user(self, email, password=None):
        #creates and save the user with the given email and password
        if not email:
            raise ValueError("user must hane a valid email address")
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser=True')
            
     #creates and saves the superuser with given email n password
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_customer = True
        user.is_seller = True
        user.is_seller_approved = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    #sellers can't use the seller pages until an admin ticks this
    is_seller_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj= None):
        #only super user have permission to access all the data
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        #only superuser has permission to view the app
        return self.is_superuser