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
    num_agregado_familiar = models.BooleanField()
    num_habit_estado = models.IntegerField

    @property
    def idade(self):
        return int((datetime.now().date() - self.data_nascimento).days / 365.25)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'moradores'

class Habitacao(models.Model):

    PUBLICA = 'PU'
    PUBLICA_PRIVADA = 'PP'
    PRIVADA = 'PR'
    OUTROS = 'OU'

    iniciativa_escolhas = [
        (PUBLICA, 'pública'),
        (PUBLICA_PRIVADA, 'pública-privada'),
        (PRIVADA, 'privada'),
        (OUTROS, 'outros')
    ]
    TIPO_T1 = 'T1'
    TIPO_T2 = 'T2'
    TIPO_T3 = 'T3'
    TIPO_T4 = 'T4'

    tipologia_escolhas = [
        (TIPO_T1, 'tipologia T1'),
        (TIPO_T2, 'tipologia T2'),
        (TIPO_T3, 'tipologia T3'),
        (TIPO_T4, 'tipologia T4'),
    ]

    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    numero_do_apartamento = models.CharField(max_length=100)
    identificacao_do_projecto = models.CharField(max_length=200)
    localizacao = models.CharField(max_length=200)
    iniciativa = models.CharField(
        max_length=2,
        choices=iniciativa_escolhas,
        default=PUBLICA
    )
    tipologia = models.CharField(
        max_length=2,
        choices=tipologia_escolhas,
        default=TIPO_T2
    )
    
    COMPRA = 'CP'
    RENDA = 'RE'
    estado_legal_escolhas = [
        (COMPRA, 'Compra'),
        (RENDA, 'Renda')
    ]

    andar = models.IntegerField()
    numero_de_compartimentos = models.IntegerField()
    estado_legal = models.CharField(
        max_length=2,
        choices=estado_legal_escolhas
    )

    alienado_ao_inh = models.BooleanField(default=True)

    def __str__(self):
        return numero_do_apartamento

    class Meta:
        verbose_name_plural = 'habitações'

