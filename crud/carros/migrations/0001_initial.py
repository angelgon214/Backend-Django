# Generated by Django 5.1.6 on 2025-02-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('plate', models.CharField(max_length=7)),
                ('color', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
