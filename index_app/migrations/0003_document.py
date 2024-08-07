# Generated by Django 4.1 on 2024-05-22 03:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('index_app', '0002_alter_news_options_alter_vacancy_options_news_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='Заголовок')),
                ('file', models.FileField(upload_to='uploads/', verbose_name='Файл')),
                ('active', models.BooleanField(default=True, verbose_name='Активна')),
            ],
            options={
                'verbose_name': 'Файл для скачивания',
                'verbose_name_plural': 'Файлы для скачивания',
                'ordering': ['-created_at'],
            },
        ),
    ]
