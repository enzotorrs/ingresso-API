# Generated by Django 4.0.1 on 2022-01-23 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0004_filme_principal_imagem_font'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('imagem', models.TextField()),
            ],
        ),
    ]
