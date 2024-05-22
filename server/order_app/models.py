from django.db import models
from server.base import (
    Directory,
    Item,
    Document
)
from auth_app.models import User
from calculator_app.models import City
from order_app.services import ganerate_new_number


class Cargo(Directory):
    name = models.CharField(
        verbose_name="Описание груза",
        max_length=255,
        null=True,
        blank=False,
        db_index=True
    )
    weight = models.DecimalField(
        verbose_name="Вес, кг", max_digits=15, decimal_places=2,
        blank=False, default=0)
    length = models.DecimalField(
        verbose_name="Длина, см", max_digits=15, decimal_places=2,
        blank=True, default=0)
    width = models.DecimalField(
        verbose_name="Ширина, см", max_digits=15, decimal_places=2,
        blank=True, default=0)
    height = models.DecimalField(
        verbose_name="Высота, см", max_digits=15, decimal_places=2,
        blank=True, default=0)
    volume = models.DecimalField(
        verbose_name="Объем, м3", max_digits=15, decimal_places=5,
        blank=False, default=0)
    seats = models.DecimalField(
        verbose_name="Количество мест, шт", max_digits=15, decimal_places=0,
        blank=False, default=1)

    def __str__(self) -> str:
        title = (f"{self.name}, Вес {self.weight} кг, "
                 f"Д{self.length}xШ{self.width}xВ{self.height} см, "
                 f"Объем {self.volume} м3, Мест {self.seats} шт")
        return title

    class Meta:
        verbose_name = "Груз"
        verbose_name_plural = "Грузы"
        ordering = ["-created_at"]


class Order(Document):

    class TimeSelector(models.TextChoices):
        T_09_19 = "t1", "09:00-19:00"
        T_19_25 = "t2", "19:00-23:00"
        T_23_08 = "t3", "23:00-08:00"

    city_from = models.ForeignKey(
        City, verbose_name="Откуда", on_delete=models.PROTECT,
        related_name="orders_from")
    from_address = models.BooleanField(
        verbose_name="Забрать по адресу", default=False)
    address_from = models.CharField(
        max_length=1024, verbose_name="Адрес забора",
        null=True, blank=True, default="")
    date_from = models.DateField(verbose_name="Дата забора")
    time_from = models.CharField(
        verbose_name="Время забора",
        max_length=2, choices=TimeSelector.choices,
        default=TimeSelector.T_09_19, blank=False)

    city_to = models.ForeignKey(
        City, verbose_name="Куда", on_delete=models.PROTECT,
        related_name="orders_to")
    to_address = models.BooleanField(
        verbose_name="Доставить по адресу", default=False)
    address_to = models.CharField(
        max_length=1024, verbose_name="Адрес доставки",
        null=True, blank=True, default="")
    date_to = models.DateField(verbose_name="Дата доставки")
    time_to = models.CharField(
        verbose_name="Время доставки",
        max_length=2, choices=TimeSelector.choices,
        default=TimeSelector.T_09_19, blank=False)

    insurance = models.BooleanField(
        verbose_name="Страхование груза", default=False)
    return_docs = models.BooleanField(
        verbose_name="Возврат пакета документов", default=False)
    declared_cost = models.DecimalField(
        verbose_name="Объявленная стоимость", max_digits=15, decimal_places=2,
        blank=True, default=0)
    cost = models.DecimalField(
        verbose_name="Стоимость", max_digits=15, decimal_places=2,
        blank=True, default=0)
    author = models.ForeignKey(
        User, verbose_name="Автор", on_delete=models.PROTECT,
        related_name="orders",
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs) -> None:
        if not self.number:
            self.number = ganerate_new_number(model=Order)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Заказ №{self.number} от {format(self.date, '%F')}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-number"]


class ItemOrder(Item):
    order = models.ForeignKey(
        Order, verbose_name="Заказ", on_delete=models.CASCADE,
        related_name="items")
    cargo = models.ForeignKey(
        Cargo, verbose_name="Груз", on_delete=models.PROTECT)
    soft_packaging = models.BooleanField(
        verbose_name="Мягкая упаковка", default=False)
    Crate = models.BooleanField(
        verbose_name="Обрешетка", default=False)
    palletizing = models.BooleanField(
        verbose_name="Паллетирование", default=False)
    pallet_board = models.BooleanField(
        verbose_name="Паллетный борт", default=False)
    seal_bag = models.BooleanField(
        verbose_name="Мешок-пломба", default=False)
    cardboard_box = models.BooleanField(
        verbose_name="Картонная коробка", default=False)
    high_security_cargo = models.BooleanField(
        verbose_name="Режимный груз", default=False)

    def __str__(self) -> str:
        return f"{self.order}"

    class Meta:
        verbose_name = "Строка заказа"
        verbose_name_plural = "Строки заказов"
        ordering = ["order"]
