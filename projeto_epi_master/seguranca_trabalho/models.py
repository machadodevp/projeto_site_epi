from django.db import models

# Create your models here.
from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    # cadastro equimento

    from django.db import models

class Equipamento(models.Model):
    # Definindo os campos do modelo de Equipamento
    nome = models.CharField(max_length=100, verbose_name="Nome do Equipamento")
    tipo = models.CharField(max_length=100, verbose_name="Tipo de Equipamento")
    validade = models.DateField(verbose_name="Data de Validade")
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade Disponível")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"

