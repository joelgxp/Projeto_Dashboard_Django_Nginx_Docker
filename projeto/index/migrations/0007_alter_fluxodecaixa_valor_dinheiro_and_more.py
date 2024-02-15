# Generated by Django 5.0 on 2024-02-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_alter_fluxodecaixa_valor_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fluxodecaixa',
            name='valor_dinheiro',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='fluxodecaixa',
            name='valor_pix',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='fluxodecaixa',
            name='valor_total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
