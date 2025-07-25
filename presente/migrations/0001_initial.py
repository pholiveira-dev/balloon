# Generated by Django 5.2.1 on 2025-06-02 01:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('imagem', models.ImageField(upload_to='produtos/')),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('data_pedido', models.DateTimeField(auto_now=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presente.produto')),
            ],
        ),
    ]
