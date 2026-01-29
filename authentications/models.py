from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class CustomUserManager(BaseUserManager):

    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('The email field must be send')
        
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('role','admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True :
            raise ValueError('Superuser must have is_active=True')
        
        return self.create_user(email=email,password=password,**extra_fields)




class CustomUser(AbstractBaseUser,PermissionsMixin):
    ROLES=[
        ('user','User'),
        ('admin','Admin'),

    ]
    email=models.EmailField(unique=True)
    role=models.CharField(max_length=20,choices=ROLES,default='user')
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    date_joined=models.DateTimeField(auto_now_add=True)

    objects=CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    

