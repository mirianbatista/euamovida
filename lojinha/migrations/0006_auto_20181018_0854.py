# Generated by Django 2.1 on 2018-10-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojinha', '0005_auto_20181018_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(upload_to='images'),
        ),
    ]