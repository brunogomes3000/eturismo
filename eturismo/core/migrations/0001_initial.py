# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-15 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='CPF')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('login', models.CharField(max_length=30, verbose_name='Login')),
                ('imagem_perfil', models.ImageField(blank=True, default='imagens/perfil/noperfil.png', null=True, upload_to='imagens/perfil', verbose_name='Imagem')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(max_length=2, verbose_name='Nota')),
                ('descricao', models.CharField(max_length=300, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Dica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=500, verbose_name='Descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=7, verbose_name='CNPJ')),
                ('descricao', models.CharField(max_length=30, verbose_name='Descrição')),
                ('site', models.CharField(max_length=40, verbose_name='Site')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=12, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=50, verbose_name='Logradouro')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('numero', models.CharField(max_length=50, verbose_name='Número')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=7, verbose_name='Latitude')),
                ('log', models.DecimalField(decimal_places=6, max_digits=7, verbose_name='Longitude')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descricao')),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Passeio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=250, verbose_name='Localização')),
                ('descricao', models.CharField(max_length=500, verbose_name='Descrição')),
                ('Distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Distrito')),
                ('Empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem_perfil', models.ImageField(blank=True, default='imagens/perfil/noperfil.png', null=True, upload_to='imagens/perfil', verbose_name='Imagem')),
                ('link', models.CharField(max_length=100, verbose_name='Link')),
                ('Distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Distrito')),
                ('Empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Dica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=1000, verbose_name='Descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Filtro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=1000, verbose_name='Descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Passeio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descricao')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
            ],
        ),
        migrations.AddField(
            model_name='tipo_dica',
            name='Tipo_Filtro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tipo_Filtro'),
        ),
        migrations.AddField(
            model_name='passeio',
            name='Tipo_Passeio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tipo_Passeio'),
        ),
        migrations.AddField(
            model_name='distrito',
            name='Municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Municipio'),
        ),
        migrations.AddField(
            model_name='dica',
            name='Distrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Distrito'),
        ),
        migrations.AddField(
            model_name='dica',
            name='Tipo_Dica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tipo_Dica'),
        ),
        migrations.AddField(
            model_name='contato',
            name='Empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresa'),
        ),
        migrations.AddField(
            model_name='contato',
            name='Tipo_Contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tipo_Contato'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='Distrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Distrito'),
        ),
    ]
