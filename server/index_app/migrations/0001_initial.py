# Generated by Django 4.1 on 2024-05-21 17:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='Заголовок')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Новость')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='Заголовок')),
                ('salary', models.CharField(max_length=50, verbose_name='Зарплата')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Новость')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]