# Generated by Django 2.1.7 on 2019-05-06 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='original',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='short',
            field=models.URLField(max_length=50),
        ),
    ]
