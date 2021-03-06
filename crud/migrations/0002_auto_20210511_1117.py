# Generated by Django 3.2 on 2021-05-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrocliente',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='uf',
            field=models.CharField(choices=[('ac', 'AC'), ('al', 'AL'), ('ap', 'AP'), ('am', 'AM'), ('ba', 'BA'), ('ce', 'CE'), ('df', 'DF'), ('es', 'ES'), ('go', 'GO'), ('ma', 'MA'), ('mt', 'MT'), ('ms', 'MS'), ('mg', 'MG'), ('pa', 'PA'), ('pb', 'PB'), ('pr', 'PR'), ('pe', 'PE'), ('pi', 'PI'), ('rj', 'RJ'), ('rn', 'RN'), ('rs', 'RS'), ('ro', 'RO'), ('rr', 'RR'), ('sc', 'SC'), ('sp', 'SP'), ('se', 'SE'), ('to', 'TO')], max_length=2),
        ),
    ]
