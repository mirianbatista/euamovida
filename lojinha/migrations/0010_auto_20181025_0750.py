# Generated by Django 2.1.2 on 2018-10-25 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lojinha', '0009_remove_produto_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ['descricao'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
    ]
