from django.db import models
from server.base import Directory


class News(Directory):
    name = models.CharField(
        verbose_name="Заголовок",
        max_length=150,
        null=True,
        blank=True,
        db_index=True
    )
    body = models.TextField(
        verbose_name="Новость",
        null=True,
        blank=True
    )
    active = models.BooleanField(
        verbose_name="Активна",
        default=True
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]


class Vacancy(Directory):
    name = models.CharField(
        verbose_name="Заголовок",
        max_length=150,
        null=True,
        blank=True,
        db_index=True
    )
    salary = models.CharField(
        max_length=50,
        verbose_name="Зарплата",
        null=True,
        blank=True
    )
    body = models.TextField(
        verbose_name="Описание вакансии",
        null=True,
        blank=True
    )
    active = models.BooleanField(
        verbose_name="Активна",
        default=True
    )

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ["-created_at"]
