# Generated by Django 5.0.1 on 2024-02-19 18:40

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import localflavor.br.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_exame', models.DateField(blank=True, null=True)),
                ('visao_le', models.IntegerField(blank=True, null=True)),
                ('visao_ld', models.IntegerField(blank=True, null=True)),
                ('correcao_visual', models.CharField(blank=True, choices=[('sim', 'SIM'), ('nao', 'NÃO')], max_length=10, null=True)),
                ('campo_visual_le', models.IntegerField(blank=True, null=True)),
                ('campo_visual_ld', models.IntegerField(blank=True, null=True)),
                ('exame_validade', models.DateField(blank=True, null=True)),
                ('conclusao', models.CharField(blank=True, choices=[('apto', 'APTO'), ('inapto', 'INAPTO')], max_length=10, null=True)),
                ('complemento', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guia', models.IntegerField(unique=True)),
                ('registro', models.CharField(max_length=9)),
                ('categoria', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('AB', 'AB'), ('AC', 'AC'), ('AD', 'AD'), ('AE', 'AE')], max_length=5)),
                ('data_cadastro', models.DateField()),
                ('data_habilitacao', models.DateField()),
                ('nome_completo', models.CharField(max_length=80)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMININO', 'FEMININO')], max_length=25)),
                ('uf_emissor', models.CharField(max_length=2)),
                ('identidade', models.CharField(max_length=25)),
                ('orgao_emissor', models.CharField(max_length=25)),
                ('uf_naturalidade', models.CharField(max_length=2)),
                ('naturalidade', models.CharField(max_length=45)),
                ('nome_mae', models.CharField(max_length=80)),
                ('nome_pai', models.CharField(max_length=80)),
                ('logradouro', models.CharField(max_length=80)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=45)),
                ('uf_cidade', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=45)),
                ('cep', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=45)),
                ('cpf', localflavor.br.models.BRCPFField(max_length=14)),
                ('celular', models.CharField(max_length=15)),
                ('hora_cadastro', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('valor_pix', models.FloatField(default=0)),
                ('valor_dinheiro', models.FloatField(default=0)),
                ('valor_total', models.FloatField(blank=True, null=True)),
                ('metodo_pagamento', models.CharField(choices=[('PIX', 'PIX'), ('DINHEIRO', 'DINHEIRO'), ('PIX/DINHEIRO', 'PIX/DINHEIRO')], max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(max_length=255)),
                ('ativo', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guia', models.IntegerField(unique=True)),
                ('solicitacao', models.CharField(choices=[('PRIMEIRA_HABILITACAO', 'PRIMEIRA HABILITAÇÃO'), ('RENOVACAO', 'RENOVAÇÃO'), ('RENOVACAO_ATIV_REM', 'RENOVAÇÃO ATIV. REMUNERADA'), ('ADICAO_CATEGORIA', 'ADIÇÃO DE CATEGORIA'), ('MUDANCA_CATEGORIA', 'MUDANÇA DE CATEGORIA'), ('ALTERACAO_DADOS', 'ALTERAÇÃO DE DADOS')], max_length=45)),
                ('data', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('id_exame', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.exame')),
                ('id_paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.paciente')),
                ('id_pagamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.pagamento')),
            ],
        ),
    ]
