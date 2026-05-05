from django.db import models

class Library(models.Model):
    """
    Модель библиотеки.
    """
    name = models.CharField(max_length=300, verbose_name="Название", help_text="Введите название библиотеки")
    address = models.CharField(max_length=300, verbose_name="Адрес", help_text="Введите название библиотеки")
    latitude = models.FloatField(verbose_name="Широта", null=True, blank=True)
    longitude = models.FloatField(verbose_name="Долгота", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", help_text="Введите описание", blank=True)
    image = models.ImageField(upload_to="libraries/", verbose_name="Фото", help_text="Добавьте фото")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Библиотека"
        verbose_name_plural = "Библиотеки"
        ordering = ["name"]

    def __str__(self):
        return self.name
