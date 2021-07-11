# Generated by Django 3.2 on 2021-07-10 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20210708_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('alteracao', models.DateTimeField(auto_now=True, verbose_name='Alterado')),
                ('nome', models.TextField(max_length=50, verbose_name='Nome fornecedor')),
                ('cep', models.IntegerField(default=0, verbose_name='CEP')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='cadastrocliente',
            name='ativo',
        ),
        migrations.AddField(
            model_name='cadastrocliente',
            name='fornecedor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crud.fornecedores'),
        ),
    ]