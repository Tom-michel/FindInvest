from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class SuperUser(BaseUserManager):
    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser')
        
        return self.create_user(email, username, password, **extra_fields)
    
    
    def create_user(self, email, username, password, **extra_fields):
        
        if not email:
            raise ValueError('the given email is not correct')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
            
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email adress', unique=True)
    username = models.CharField(max_length=255, blank=True) 
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True)
    
    objects = SuperUser()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
    
