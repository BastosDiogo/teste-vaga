# Generated by Django 4.1 on 2023-10-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_produtos_categoria_alter_produtos_fornecedores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='descricao',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
