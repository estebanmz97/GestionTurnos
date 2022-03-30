from django.db import models

# Create your models here.

# Agregue las clases y las migre a la base de datos con python manage.py makemigrations
class Paciente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Medico(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
 
class Administrador(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Turno(models.Model):
    nombre= models.CharField(max_length=30)
    fecha = models.DateField()  
    confirmado = models.BooleanField()