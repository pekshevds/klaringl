# Generated by Django 4.1 on 2024-05-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0005_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$lsqm5GMv28aXzBDWujhh4G$oqLPXeDJhaYVzWF7KjIl7+yGXQuS0Bq3yNDjVdW3Y0Y=', max_length=128, verbose_name='password'),
        ),
    ]
