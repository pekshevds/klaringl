from django.db import models
from server.base import Directory


class Branch(Directory):

    address = models.CharField(
        verbose_name="Адрес",
        max_length=255,
        blank=True,
        null=True,
        default=""
    )

    email = models.EmailField(
        verbose_name="Электронная почта",
        max_length=50,
        blank=True,
        null=True,
        default=""
    )
    tel = models.CharField(
        verbose_name="Телефон",
        max_length=25,
        blank=True,
        null=True,
        default=""
    )
    active = models.BooleanField(
        verbose_name="Активен",
        default=True
    )

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"
        ordering = ["-created_at"]
