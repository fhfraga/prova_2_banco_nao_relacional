from django.contrib.auth.models import User
from django.db import models


class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    instrutor = models.CharField(max_length=50)
    data_inicio = models.DateField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    

    def __str__(self):
        return self.titulo