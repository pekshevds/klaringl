from datetime import datetime
import uuid
from django.db import models
from django.utils.dateformat import format


class TimeSelector(models.TextChoices):
    T_09_19 = "t1", "09:00-19:00"
    T_19_25 = "t2", "19:00-23:00"
    T_23_08 = "t3", "23:00-08:00"


class FormOfOwnershipSelector(models.TextChoices):
    FZ = "FZ", "Физическое лицо"
    IP = "IP", "Индивидуальный предприниматель"
    OR = "OR", "Физическое лицо"


class PayerSelector(models.TextChoices):
    SD = "SD", "Отправитель"
    RP = "RP", "Получатель"
    PR = "PR", "Третье лицо"


class Item(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения",
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class Base(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    comment = models.TextField(
        verbose_name="Комментарий",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения",
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class Directory(Base):
    name = models.CharField(
        verbose_name="Наименование",
        max_length=150,
        null=True,
        blank=True,
        db_index=True
    )

    def __str__(self) -> str:
        return f"{self.name}"

    @classmethod
    def find_by_name(cls, name: str):
        return cls.objects.filter(name=name).first()

    class Meta:
        abstract = True


class Document(Base):
    number = models.IntegerField(
        verbose_name="Номер",
        null=True,
        blank=True,
        editable=False,
        default=0
    )
    date = models.DateTimeField(
        verbose_name="Дата",
        null=True,
        blank=True,
        default=datetime.now
    )

    def __str__(self) -> str:
        return f"Документ №{self.id} от {format(self.date, '%Y.%m.%d')}"

    class Meta:
        abstract = True
