# Generated by Django 5.2 on 2025-04-25 16:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguranca_trabalho', '0004_equipamento_fabricante'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipamento',
            options={},
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='email',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='idade',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='telefone',
        ),
        migrations.RemoveField(
            model_name='equipamento',
            name='fabricante',
        ),
        migrations.RemoveField(
            model_name='equipamento',
            name='numero_serie',
        ),
        migrations.RemoveField(
            model_name='equipamento',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Acao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField(default=django.utils.timezone.now)),
                ('data_prevista_devolucao', models.DateField()),
                ('status', models.CharField(choices=[('Emprestado', 'Emprestado'), ('Em uso', 'Em uso'), ('Fornecido', 'Fornecido'), ('Devolvido', 'Devolvido'), ('Danificado', 'Danificado'), ('Perdido', 'Perdido')], max_length=20)),
                ('condicoes_emprestimo', models.TextField()),
                ('data_devolucao', models.DateField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguranca_trabalho.colaborador')),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguranca_trabalho.equipamento')),
            ],
        ),
    ]
