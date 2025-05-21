from django.db import models
from customers.models import User

class Condominium(models.Model):
    name       = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Bloc(models.Model):
    condominium = models.ForeignKey(Condominium, on_delete=models.CASCADE, related_name='blocos')
    number_bloc = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Unit(models.Model):
    bloc   = models.ForeignKey(Bloc, on_delete=models.CASCADE, related_name='unidades')
    number = models.CharField(max_length=10)

    def __str__(self):
        return f"Unidade {self.number} - {self.bloc.name}"
    
    
class Warning(models.Model):
    title       = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    author      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avisos')
    created_at  = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    

class Event(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField()
    author      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos')
    unit        = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='ocorrencias')
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
