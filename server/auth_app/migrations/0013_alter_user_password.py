# Generated by Django 4.1 on 2024-05-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0012_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$r749SoiIb0Sr900HFMRY3U$yNmjTtkJl0IEap+S2tbUzZgzkRgQwU+VqGzfGADR7ZI=', max_length=128, verbose_name='password'),
        ),
    ]