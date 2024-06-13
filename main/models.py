# main/models.py
from django.db import models

class Alumno(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    nombre = models.TextField()
    apellidoPat = models.TextField()
    apellidoMat = models.TextField()
    password = models.TextField()

class Profesor(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    nombre = models.TextField()
    apellidoPat = models.TextField()
    apellidoMat = models.TextField()
    password = models.TextField()

class Materia(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()

class Calificacion(models.Model):
    id = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    cal = models.FloatField()
    

