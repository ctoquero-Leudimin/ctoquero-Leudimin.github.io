# Generated by Django 4.1.4 on 2023-02-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cortacesped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=64)),
                ('descripcion', models.CharField(max_length=128)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Desbrozadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=64)),
                ('descripcion', models.CharField(max_length=128)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Motosierra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=64)),
                ('descripcion', models.CharField(max_length=128)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]