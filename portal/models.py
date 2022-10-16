from unittest.util import _MAX_LENGTH
from django.db import models
# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

