# Generated by Django 4.1 on 2024-06-20 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0033_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$m8aWJS91wjNqgY0bzufmAh$bQaS9K4JrbSwjWUVSV49iNTKVlLy3oNcIpFNgqd5uNs=', max_length=128, verbose_name='password'),
        ),
    ]