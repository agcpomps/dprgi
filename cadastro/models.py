from django.db import models
from datetime import datetime

# Create your models here.
class Morador(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    bi = models.CharField(max_length=14)
    nif = models.CharField(max_length=16)
    estado_civil = models.BooleanField(default=False)
    profissao = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    funcionario_publico = models.BooleanField(default=False)
    local_de_trabalho = models.CharField(max_length=200)
    salario_base = models.DecimalField(max_digits=6, decimal_places=2)
    num_agregado_familiar = models.ImageField()
    num_habit_estado = models.IntegerField

    @property
    def idade(self):
        return int((datetime.now().date() - self.data_nascimento).days / 365.25)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'moradores'

