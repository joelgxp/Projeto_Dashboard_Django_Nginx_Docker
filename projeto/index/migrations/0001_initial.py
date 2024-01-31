# Generated by Django 4.2.1 on 2024-01-31 00:30

from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PacienteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guia', models.IntegerField()),
                ('registro', models.IntegerField()),
                ('categoria', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('AB', 'AB'), ('AC', 'AC'), ('AD', 'AD'), ('AE', 'AE')], max_length=5)),
                ('solicitacao', models.CharField(choices=[('PRIMEIRA_HABILITACAO', 'Primeira Habilitação'), ('RENOVACAO', 'Renovação'), ('ADICAO_CATEGORIA', 'Adição de Categoria'), ('MUDANCA_CATEGORIA', 'Mudança de Categoria')], max_length=25)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_habilitacao', models.DateField()),
                ('nome_completo', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(choices=[('MASCULINO', 'Masculino'), ('FEMININO', 'Feminino')], max_length=25)),
                ('identidade', models.CharField(max_length=25)),
                ('orgao_emissor', models.CharField(max_length=25)),
                ('uf_emissor', models.CharField(max_length=25)),
                ('naturalidade', models.CharField(max_length=45)),
                ('uf_naturalidade', models.CharField(max_length=25)),
                ('nome_mae', models.CharField(max_length=200)),
                ('nome_pai', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=15)),
                ('cpf', localflavor.br.models.BRCPFField(blank=True, max_length=14)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=45)),
                ('cidade', models.CharField(max_length=45)),
                ('cep', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=45)),
                ('uf_cidade', models.CharField(max_length=25)),
                ('atendido', models.BooleanField(default=False)),
                ('hora_cadastro', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=255)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
