# Generated by Django 4.0.1 on 2022-01-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0003_filme_principal'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='principal_imagem_font',
            field=models.TextField(null=True, default=None),
            preserve_default=False,
        ),
    ]