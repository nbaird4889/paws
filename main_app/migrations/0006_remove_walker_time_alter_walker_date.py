# Generated by Django 4.0.2 on 2022-02-16 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_walker_dog_walker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='walker',
            name='time',
        ),
        migrations.AlterField(
            model_name='walker',
            name='date',
            field=models.DateField(verbose_name='Working On:'),
        ),
    ]
