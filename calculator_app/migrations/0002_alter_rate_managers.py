# Generated by Django 4.1 on 2024-05-27 09:56

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('calculator_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='rate',
            managers=[
                ('cities_from', django.db.models.manager.Manager()),
            ],
        ),
    ]
