# Generated by Django 2.2.7 on 2019-11-27 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20191127_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='Article', verbose_name='Imagen'),
        ),
    ]
