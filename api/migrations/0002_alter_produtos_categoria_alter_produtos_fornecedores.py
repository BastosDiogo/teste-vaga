# Generated by Django 4.1 on 2023-10-11 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoria'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='fornecedores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fornecedor'),
        ),
    ]
