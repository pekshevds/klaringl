# Generated by Django 4.1 on 2024-05-27 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0022_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$xSVhUVYSbTuXNtA73zEUM8$EbAYnZQRQLHNoIJjA5btMakLaznn7MSuqi3DKxYLXzo=', max_length=128, verbose_name='password'),
        ),
    ]