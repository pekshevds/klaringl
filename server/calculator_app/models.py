from django.db import models
from django.db.models import Count
from server.base import (
    Directory,
    Base
)


class City(Directory):
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ["name"]


class RateItem(Directory):
    class Meta:
        verbose_name = "Статья тарифа"
        verbose_name_plural = "Статьи тарифов"
        ordering = ["name"]


class LastMileRate(Directory):
    rate_item = models.ForeignKey(
        RateItem,
        verbose_name="Статья",
        on_delete=models.PROTECT,
        related_name="rate_items",
        null=True
    )
    cost_by_weight_0_25 = models.DecimalField(
        verbose_name="<25", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_25_50 = models.DecimalField(
        verbose_name="<50", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_50_150 = models.DecimalField(
        verbose_name="51-150", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_150_300 = models.DecimalField(
        verbose_name="151-300", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_300_500 = models.DecimalField(
        verbose_name="301-500", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_500_1000 = models.DecimalField(
        verbose_name="501-1000", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_1000_1500 = models.DecimalField(
        verbose_name="1001-1500", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_1500_2000 = models.DecimalField(
        verbose_name="1501-2000", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_2000_3000 = models.DecimalField(
        verbose_name="2001-3000", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_3000_5000 = models.DecimalField(
        verbose_name="3001-5000", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_5000_10000 = models.DecimalField(
        verbose_name="5001-10000", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_10000_20000 = models.DecimalField(
        verbose_name="10000-20000", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_20000_inf = models.DecimalField(
        verbose_name=">20000", max_digits=15, decimal_places=2,
        blank=True, default=0)

    cost_by_volume_0_01 = models.DecimalField(
        verbose_name="<0.1", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_01_02 = models.DecimalField(
        verbose_name="<0.2", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_02_06 = models.DecimalField(
        verbose_name="0.2-0.6", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_06_12 = models.DecimalField(
        verbose_name="0.6-1.2", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_12_20 = models.DecimalField(
        verbose_name="1.2-2.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_20_40 = models.DecimalField(
        verbose_name="2.0-4.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_40_60 = models.DecimalField(
        verbose_name="4.0-6.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_60_80 = models.DecimalField(
        verbose_name="6.0-8.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_80_120 = models.DecimalField(
        verbose_name="8.0-12.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_120_200 = models.DecimalField(
        verbose_name="12.0-20.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_200_400 = models.DecimalField(
        verbose_name="20.0-40.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_400_800 = models.DecimalField(
        verbose_name="40.0-80.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_800_inf = models.DecimalField(
        verbose_name=">80.0", max_digits=15, decimal_places=2,
        blank=True, default=0)

    def __str__(self) -> str:
        return f"{self.city_from.name} - {self.city_to.name}"

    class Meta:
        verbose_name = "Тариф на экспедирование'"
        verbose_name_plural = "Тарифы на экспедирование"
        ordering = ["rate_item"]


class CityFromManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        rate = super().get_queryset().\
            values_list("city_from", flat=True).distinct()
        cities = City.objects.filter(id__in=rate)
        return cities


class CityToManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        rate = super().get_queryset().\
            values_list("city_to", flat=True).distinct()
        cities = City.objects.filter(id__in=rate)
        return cities


class Rate(Base):
    city_from = models.ForeignKey(
        City,
        verbose_name="Город отправитель",
        on_delete=models.PROTECT,
        related_name="cities_from",
        null=True
    )
    city_to = models.ForeignKey(
        City,
        verbose_name="Город получатель",
        on_delete=models.PROTECT,
        related_name="cities_to",
        null=True
    )
    delivery_time = models.CharField(
        verbose_name="Срок доставки",
        max_length=25,
        blank=True,
        default=""
    )
    shipping_schedule = models.CharField(
        verbose_name="График отправок",
        max_length=25,
        blank=True,
        default=""
    )
    cost_by_weight_0_25 = models.DecimalField(
        verbose_name="<25", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_25_50 = models.DecimalField(
        verbose_name="<50", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_50_150 = models.DecimalField(
        verbose_name="51-150", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_150_300 = models.DecimalField(
        verbose_name="151-300", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_300_500 = models.DecimalField(
        verbose_name="301-500", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_500_1000 = models.DecimalField(
        verbose_name="501-1000", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_1000_1500 = models.DecimalField(
        verbose_name="1001-1500", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_1500_2000 = models.DecimalField(
        verbose_name="1501-2000", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_2000_3000 = models.DecimalField(
        verbose_name="2001-3000", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_3000_5000 = models.DecimalField(
        verbose_name="3001-5000", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_5000_10000 = models.DecimalField(
        verbose_name="5001-10000", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_weight_10000_inf = models.DecimalField(
        verbose_name=">10000", max_digits=15, decimal_places=2,
        blank=True, default=0)

    cost_by_volume_0_01 = models.DecimalField(
        verbose_name="<0.1", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_01_02 = models.DecimalField(
        verbose_name="<0.2", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_02_06 = models.DecimalField(
        verbose_name="0.2-0.6", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_06_12 = models.DecimalField(
        verbose_name="0.6-1.2", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_12_20 = models.DecimalField(
        verbose_name="1.2-2.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_20_40 = models.DecimalField(
        verbose_name="2.0-4.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_40_60 = models.DecimalField(
        verbose_name="4.0-6.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_60_80 = models.DecimalField(
        verbose_name="6.0-8.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_80_120 = models.DecimalField(
        verbose_name="8.0-12.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_120_200 = models.DecimalField(
        verbose_name="12.0-20.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_200_400 = models.DecimalField(
        verbose_name="20.0-40.0", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost_by_volume_400_inf = models.DecimalField(
        verbose_name=">40.0", max_digits=15, decimal_places=2,
        blank=True, default=0)

    cities_from = CityFromManager()
    cities_to = CityToManager()
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.city_from.name} - {self.city_to.name}"

    class Meta:
        verbose_name = "Тариф магистральный"
        verbose_name_plural = "Тарифы магистральные"
        ordering = ["city_from", "city_to"]
