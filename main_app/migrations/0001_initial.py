# Generated by Django 4.0.2 on 2022-02-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('size', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
