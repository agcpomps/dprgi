# Generated by Django 3.0.4 on 2020-03-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Morador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField()),
                ('bi', models.CharField(max_length=14)),
                ('nif', models.CharField(max_length=16)),
                ('estado_civil', models.BooleanField(default=False)),
                ('profissao', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('funcionario_publico', models.BooleanField(default=False)),
                ('local_de_trabalho', models.CharField(max_length=200)),
                ('salario_base', models.DecimalField(decimal_places=2, max_digits=6)),
                ('num_agregado_familiar', models.ImageField(upload_to='')),
            ],
        ),
    ]
