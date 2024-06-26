# Generated by Django 4.1 on 2024-05-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['-created_at'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AddField(
            model_name='news',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активна'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='body',
            field=models.TextField(blank=True, null=True, verbose_name='Описание вакансии'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Зарплата'),
        ),
    ]
