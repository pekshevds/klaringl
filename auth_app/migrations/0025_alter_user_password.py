# Generated by Django 4.1 on 2024-05-29 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0024_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$1LFsckE6tnZvQ0xVtVJjw3$sHD2Ns+KFbDL/WBQNGitRdlf+TBvSL8gOT7sMIr+Bb4=', max_length=128, verbose_name='password'),
        ),
    ]