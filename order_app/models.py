from django.db import models
from server.base import (
    Directory,
    Item,
    Document,
    FormOfOwnershipSelector,
    PayerSelector,
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
        db_index=True,
    )
    weight = models.DecimalField(
        verbose_name="Вес, кг", max_digits=15, decimal_places=2, blank=False, default=0
    )
    length = models.DecimalField(
        verbose_name="Длина, см", max_digits=15, decimal_places=2, blank=True, default=0
    )
    width = models.DecimalField(
        verbose_name="Ширина, см",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    height = models.DecimalField(
        verbose_name="Высота, см",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    volume = models.DecimalField(
        verbose_name="Объем, м3",
        max_digits=15,
        decimal_places=5,
        blank=False,
        default=0,
    )

    def __str__(self) -> str:
        title = (
            f"{self.name}, Вес {self.weight} кг, "
            f"Д{self.length}xШ{self.width}xВ{self.height} см, "
            f"Объем {self.volume} м3"
        )
        return title

    class Meta:
        verbose_name = "Груз"
        verbose_name_plural = "Грузы"
        ordering = ["-created_at"]


class Order(Document):
    # Основные реквизиты отправителя
    city_from = models.ForeignKey(
        City,
        verbose_name="Откуда",
        on_delete=models.PROTECT,
        related_name="orders_from",
    )
    from_address = models.BooleanField(verbose_name="Забрать по адресу", default=False)
    address_from = models.CharField(
        max_length=1024, verbose_name="Адрес забора", null=True, blank=True, default=""
    )
    date_from = models.DateField(verbose_name="Дата забора", null=True, blank=True)
    from_time = models.BooleanField(verbose_name="Забрать по времени", default=False)
    time_from = models.TimeField(verbose_name="Время забора", null=True, blank=True)

    form_from = models.CharField(
        verbose_name="Форма собственности",
        max_length=2,
        choices=FormOfOwnershipSelector.choices,
        default=FormOfOwnershipSelector.FZ,
        blank=False,
    )
    name_from = models.CharField(
        max_length=255, verbose_name="Наименование", null=True, blank=True, default=""
    )
    face_from = models.CharField(
        max_length=255,
        verbose_name="Контактное лицо",
        null=True,
        blank=True,
        default="",
    )
    tel_from = models.CharField(
        max_length=25, verbose_name="Телефон", null=True, blank=True, default=""
    )
    email_from = models.EmailField(
        max_length=25, verbose_name="E-Mail", null=True, blank=True
    )

    # Основные реквизиты получателя
    city_to = models.ForeignKey(
        City, verbose_name="Куда", on_delete=models.PROTECT, related_name="orders_to"
    )
    to_address = models.BooleanField(verbose_name="Доставить по адресу", default=False)
    address_to = models.CharField(
        max_length=1024,
        verbose_name="Адрес доставки",
        null=True,
        blank=True,
        default="",
    )
    date_to = models.DateField(verbose_name="Дата доставки", null=True, blank=True)
    to_time = models.BooleanField(verbose_name="Доставить ко времени", default=False)
    time_to = models.TimeField(verbose_name="Время доставки", null=True, blank=True)

    form_to = models.CharField(
        verbose_name="Форма собственности",
        max_length=2,
        choices=FormOfOwnershipSelector.choices,
        default=FormOfOwnershipSelector.FZ,
        blank=False,
    )
    name_to = models.CharField(
        max_length=255, verbose_name="Наименование", null=True, blank=True, default=""
    )
    face_to = models.CharField(
        max_length=255,
        verbose_name="Контактное лицо",
        null=True,
        blank=True,
        default="",
    )
    tel_to = models.CharField(
        max_length=25, verbose_name="Телефон", null=True, blank=True, default=""
    )
    email_to = models.EmailField(
        max_length=25, verbose_name="E-Mail", null=True, blank=True
    )

    # Реквизиты плательщика
    payer = models.CharField(
        verbose_name="Плательщик",
        max_length=2,
        choices=PayerSelector.choices,
        default=PayerSelector.SD,
        blank=False,
    )
    form_payer = models.CharField(
        verbose_name="Форма собственности",
        max_length=2,
        choices=FormOfOwnershipSelector.choices,
        default=FormOfOwnershipSelector.FZ,
        blank=False,
    )
    name_payer = models.CharField(
        max_length=255, verbose_name="Наименование", null=True, blank=True, default=""
    )
    face_payer = models.CharField(
        max_length=255,
        verbose_name="Контактное лицо",
        null=True,
        blank=True,
        default="",
    )
    tel_payer = models.CharField(
        max_length=25, verbose_name="Телефон", null=True, blank=True, default=""
    )
    email_payer = models.EmailField(
        max_length=25, verbose_name="E-Mail", null=True, blank=True
    )

    insurance = models.BooleanField(verbose_name="Страхование груза", default=False)
    return_docs = models.BooleanField(
        verbose_name="Возврат пакета документов", default=False
    )
    declared_cost = models.DecimalField(
        verbose_name="Объявленная стоимость",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    cost = models.DecimalField(
        verbose_name="Стоимость", max_digits=15, decimal_places=2, blank=True, default=0
    )
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.PROTECT,
        related_name="orders",
        null=True,
        blank=True,
    )
    uploaded = models.BooleanField(verbose_name="Выгружен в 1С", default=False)

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
        Order, verbose_name="Заказ", on_delete=models.CASCADE, related_name="items"
    )
    cargo = models.ForeignKey(Cargo, verbose_name="Груз", on_delete=models.PROTECT)
    hard_packaging = models.BooleanField(verbose_name="Жесткая упаковка", default=False)
    soft_packaging = models.BooleanField(verbose_name="Мягкая упаковка", default=False)
    palletizing = models.BooleanField(verbose_name="Паллетирование", default=False)
    prr_from = models.BooleanField(
        verbose_name="Погрузка при заборе груза (ПРР при заборе)", default=False
    )
    prr_to = models.BooleanField(
        verbose_name="Выгрузка при доставке (ПРР при доставке)", default=False
    )

    def __str__(self) -> str:
        return f"{self.order}"

    class Meta:
        verbose_name = "Строка заказа"
        verbose_name_plural = "Строки заказов"
        ordering = ["order"]
