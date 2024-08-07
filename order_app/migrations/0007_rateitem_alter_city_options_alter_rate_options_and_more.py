# Generated by Django 4.1 on 2024-05-15 10:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0006_rename_cost_by_volume_40_inf_rate_cost_by_volume_400_inf_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Статья тарифа',
                'verbose_name_plural': 'Статьи тарифов',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'ordering': ['city_from', 'city_to'], 'verbose_name': 'Тариф', 'verbose_name_plural': 'Тарифы'},
        ),
        migrations.CreateModel(
            name='LastMileRate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='Наименование')),
                ('cost_by_weight_0_25', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='<25')),
                ('cost_by_weight_25_50', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='<50')),
                ('cost_by_weight_50_150', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='51-150')),
                ('cost_by_weight_150_300', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='151-300')),
                ('cost_by_weight_300_500', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='301-500')),
                ('cost_by_weight_500_1000', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='501-1000')),
                ('cost_by_weight_1000_1500', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='1001-1500')),
                ('cost_by_weight_1500_2000', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='1501-2000')),
                ('cost_by_weight_2000_3000', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='2001-3000')),
                ('cost_by_weight_3000_5000', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='3001-5000')),
                ('cost_by_weight_5000_10000', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='5001-10000')),
                ('cost_by_weight_10000_20000', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='10000-20000')),
                ('cost_by_weight_20000_inf', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='>20000')),
                ('cost_by_volume_0_01', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='<0.1')),
                ('cost_by_volume_01_02', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='<0.2')),
                ('cost_by_volume_02_06', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='0.2-0.6')),
                ('cost_by_volume_06_12', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='0.6-1.2')),
                ('cost_by_volume_12_20', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='1.2-2.0')),
                ('cost_by_volume_20_40', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='2.0-4.0')),
                ('cost_by_volume_40_60', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='4.0-6.0')),
                ('cost_by_volume_60_80', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='6.0-8.0')),
                ('cost_by_volume_80_120', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='8.0-12.0')),
                ('cost_by_volume_120_200', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='12.0-20.0')),
                ('cost_by_volume_200_400', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='20.0-40.0')),
                ('cost_by_volume_400_800', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='40.0-80.0')),
                ('cost_by_volume_800_inf', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='>80.0')),
                ('rate_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rate_items', to='order_app.rateitem', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Тариф на забор/доставку грузов',
                'verbose_name_plural': 'Тарифы на забор/доставку грузов',
                'ordering': ['rate_item'],
            },
        ),
    ]
