from django.db import models

# Create your models here.
class Funcionario(models.Model):

    nome = models.CharField(max_length=255, null=False, blank=True)
    sobreNome = models.CharField(max_length=255, null=False, blank=True)
    cpf = models.CharField(max_length=255, null=False, blank=True)
    tempo_de_servico = models.PositiveIntegerField(default=0, null=False, blank=True)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2)

    objetos = models.Manager()
 