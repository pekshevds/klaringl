from decimal import Decimal
from collections import namedtuple
from django.db import models
from server.base import Directory, Base
from auth_app.models import User


class Const(Base):
    address = models.CharField(
        verbose_name="Адрес", max_length=255, blank=True, null=True, default=""
    )

    email = models.CharField(
        verbose_name="Электронная почта",
        max_length=50,
        blank=True,
        null=True,
        default="",
    )
    tel = models.CharField(
        verbose_name="Телефон", max_length=25, blank=True, null=True, default=""
    )
    nigth_deliver_cost = models.DecimalField(
        verbose_name="Тариф ночной доставки (21.00-09.00), руб",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    time_deliver_cost = models.DecimalField(
        verbose_name="Доставка ко времени, руб",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    warehouse_process_cost = models.DecimalField(
        verbose_name="Складская обработка грузов, руб/м3",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    min_warehouse_process_cost = models.DecimalField(
        verbose_name="Минимальная стоимость складской обработки грузов, руб",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    return_docs_cost = models.DecimalField(
        verbose_name="Возврат документов, руб",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    insurance_cost = models.DecimalField(
        verbose_name="Страхование, %",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    prr_cost = models.DecimalField(
        verbose_name="Услуга ПРР, руб",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    hard_packaging_cost = models.DecimalField(
        verbose_name="Жесткая упаковка (обрешётка), руб",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    hard_packaging_min_cost = models.DecimalField(
        verbose_name="Жесткая упаковка (обрешётка) минимальная стоимость, руб",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    soft_packaging_cost = models.DecimalField(
        verbose_name="Мягкая упаковка (пупырка), руб",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )
    palletizing_cost = models.DecimalField(
        verbose_name="Стоимость паллетирования, руб",
        max_digits=15,
        decimal_places=2,
        blank=True,
        default=0,
    )

    def save(self, *args, **kwargs):
        """
        Синглтон - обеспечивает наличие не более одной записи"""
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    @classmethod
    def info(cls):
        Const = namedtuple(
            "Const",
            [
                "address",
                "email",
                "tel",
                "nigth_deliver_cost",
                "time_deliver_cost",
                "warehouse_process_cost",
                "min_warehouse_process_cost",
                "return_docs_cost",
                "insurance_cost",
                "prr_cost",
                "hard_packaging_cost",
                "hard_packaging_min_cost",
                "soft_packaging_cost",
                "palletizing_cost",
            ],
        )
        Decimal0 = Decimal("0")
        item = cls.objects.first()
        if item:
            return Const(
                address=item.address,
                email=item.email,
                tel=item.tel,
                nigth_deliver_cost=item.nigth_deliver_cost,
                time_deliver_cost=item.time_deliver_cost,
                warehouse_process_cost=item.warehouse_process_cost,
                min_warehouse_process_cost=item.min_warehouse_process_cost,
                return_docs_cost=item.return_docs_cost,
                insurance_cost=item.insurance_cost,
                prr_cost=item.prr_cost,
                hard_packaging_cost=item.hard_packaging_cost,
                hard_packaging_min_cost=item.hard_packaging_min_cost,
                soft_packaging_cost=item.soft_packaging_cost,
                palletizing_cost=item.palletizing_cost,
            )
        return Const(
            address="",
            email="",
            tel="",
            nigth_deliver_cost=Decimal0,
            time_deliver_cost=Decimal0,
            warehouse_process_cost=Decimal0,
            min_warehouse_process_cost=Decimal0,
            return_docs_cost=Decimal0,
            insurance_cost=Decimal0,
            prr_cost=Decimal0,
            hard_packaging_cost=Decimal0,
            hard_packaging_min_cost=Decimal0,
            soft_packaging_cost=Decimal0,
            palletizing_cost=Decimal0,
        )

    class Meta:
        verbose_name = "Константы"
        verbose_name_plural = "Константы"
        ordering = ["-created_at"]


class Tag(Directory):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["-created_at"]


class LastNewsManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(active=True)[:3]


class ActiveNewsManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(active=True)


class News(Directory):
    name = models.CharField(
        verbose_name="Заголовок", max_length=150, null=True, blank=True, db_index=True
    )
    body = models.TextField(verbose_name="Новость", null=True, blank=True)
    tag = models.ForeignKey(
        Tag,
        verbose_name="tag",
        on_delete=models.PROTECT,
        related_name="news",
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.PROTECT,
        related_name="news",
        null=True,
        blank=True,
    )
    active = models.BooleanField(verbose_name="Активна", default=True)

    objects = models.Manager()
    last_news = LastNewsManager()
    active_news = ActiveNewsManager()

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]


class ActiveVacancyManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(active=True)


class Vacancy(Directory):
    name = models.CharField(
        verbose_name="Заголовок", max_length=150, null=True, blank=True, db_index=True
    )
    salary = models.CharField(
        max_length=50, verbose_name="Зарплата", null=True, blank=True
    )
    body = models.TextField(verbose_name="Описание вакансии", null=True, blank=True)
    active = models.BooleanField(verbose_name="Активна", default=True)

    objects = models.Manager()
    active_vacancies = ActiveVacancyManager()

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ["-created_at"]


class ActiveBranchManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(active=True)


class Branch(Directory):
    address = models.CharField(
        verbose_name="Адрес", max_length=255, blank=True, null=True, default=""
    )

    email = models.EmailField(
        verbose_name="Электронная почта",
        max_length=50,
        blank=True,
        null=True,
        default="",
    )
    tel = models.CharField(
        verbose_name="Телефон", max_length=25, blank=True, null=True, default=""
    )
    active = models.BooleanField(verbose_name="Активен", default=True)

    objects = models.Manager()
    active_branchs = ActiveBranchManager()

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"
        ordering = ["-created_at"]


class ActiveDocumentManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(active=True)


class Document(Directory):
    name = models.CharField(
        verbose_name="Заголовок", max_length=150, null=True, blank=True, db_index=True
    )
    file = models.FileField(verbose_name="Файл", upload_to="uploads/")
    active = models.BooleanField(verbose_name="Активна", default=True)

    objects = models.Manager()
    active_documents = ActiveDocumentManager()

    class Meta:
        verbose_name = "Файл для скачивания"
        verbose_name_plural = "Файлы для скачивания"
        ordering = ["-created_at"]
