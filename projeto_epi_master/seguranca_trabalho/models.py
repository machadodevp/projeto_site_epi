from django.db import models
from django.utils import timezone

# Create your models here.

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(default=0)
    email = models.EmailField(default='sem_email@exemplo.com')
    telefone = models.CharField(max_length=15, default='0000-0000')
    cargo = models.CharField(max_length=50, default='Sem cargo')


    def __str__(self):
        return self.nome

    # cadastro equimento

class Equipamento(models.Model):
    # Definindo os campos do modelo de Equipamento
    nome = models.CharField(max_length=100, verbose_name="Nome do Equipamento")
    tipo = models.CharField(max_length=100, verbose_name="Tipo de Equipamento", default="Desconhecido")
    numero_serie = models.CharField(max_length=100, default='DEFAULT123')
    fabricante = models.CharField(max_length=100, default='DEFAULT123')
   
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"




STATUS_CHOICES = [
    ('Emprestado', 'Emprestado'),
    ('Em uso', 'Em uso'),
    ('Fornecido', 'Fornecido'),
    ('Devolvido', 'Devolvido'),
    ('Danificado', 'Danificado'),
    ('Perdido', 'Perdido'),
]

# -----------------Tela de controle de epi-------------------------------
class Acao(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(default=timezone.now)
    data_prevista_devolucao = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    condicoes_emprestimo = models.TextField()
    data_devolucao = models.DateField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.equipamento.nome} para {self.colaborador.nome}"
