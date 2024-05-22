from django.db import models
from server.base import Directory, Base
from auth_app.models import User


class Const(Base):
    address = models.CharField(
        verbose_name="Адрес",
        max_length=255,
        blank=True,
        null=True,
        default=""
    )

    email = models.CharField(
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

    def save(self, *args, **kwargs):
        """
        Синглтон - обеспечивает наличие не более одной записи"""
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    @classmethod
    def info(cls):
        data = {
            "address": "",
            "email": "",
            "tel": ""
        }
        item = cls.objects.first()
        if item:
            data["address"] = item.address
            data["email"] = item.email
            data["tel"] = item.tel
        return data

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
    tag = models.ForeignKey(
        Tag, verbose_name="tag", on_delete=models.PROTECT,
        related_name="news",
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        User, verbose_name="Автор", on_delete=models.PROTECT,
        related_name="news",
        null=True,
        blank=True
    )
    active = models.BooleanField(
        verbose_name="Активна",
        default=True
    )

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

    objects = models.Manager()
    active_vacancies = ActiveVacancyManager()

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ["-created_at"]


class ActiveDocumentManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(active=True)


class Document(Directory):
    name = models.CharField(
        verbose_name="Заголовок",
        max_length=150,
        null=True,
        blank=True,
        db_index=True
    )
    file = models.FileField(
        verbose_name="Файл",
        upload_to="uploads/"
    )
    active = models.BooleanField(
        verbose_name="Активна",
        default=True
    )

    objects = models.Manager()
    active_documents = ActiveDocumentManager()

    class Meta:
        verbose_name = "Файл для скачивания"
        verbose_name_plural = "Файлы для скачивания"
        ordering = ["-created_at"]
