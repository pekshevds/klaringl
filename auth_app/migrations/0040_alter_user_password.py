# Generated by Django 4.1 on 2024-07-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0039_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$299TCQcrbDhSMhHv6FZvay$4PBTEJjto376xXYIa6kX3ZVnY86dZKMn4uEaIPPFgHk=', max_length=128, verbose_name='password'),
        ),
    ]
