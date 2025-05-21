from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from condominium.models import Unit

class User(models.Model):
    
    TYPE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('SYNDIC', 'Síndico'),
        ('RESIDENT', 'Morador')
    )
    
    GENDER = (
        ('MALE', 'Masculino'),
        ('FEMALE', 'Feminino'),
        ('OTHERS', 'Outros')
    )
    
    type          = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Morador')
    email         = models.EmailField(null=True, blank=True)
    cpf           = models.CharField(max_length=15, unique=True)
    whatsapp      = models.CharField(max_length=255, null=True, blank=True)
    birth_date    = models.DateField(null=True, blank=True)
    gender        = models.CharField(max_length=255, choices=GENDER, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    unit          = models.ForeignKey('condominium.Unit', on_delete=models.SET_NULL, null=True, blank=True, related_name='unidade')
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    
