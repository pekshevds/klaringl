# Generated by Django 4.1 on 2024-06-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0030_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$Althbdk7hKPN8azA93GGEM$ZxjFbCDVW1mK0EJoFy8uDxQskARIGc0Y53NWCIZaF7U=', max_length=128, verbose_name='password'),
        ),
    ]
