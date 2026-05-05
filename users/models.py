from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Модель пользователя. В качестве логина используется email.
    """
    username = None

    class Role(models.TextChoices):
        USER = "user", "Пользователь"
        ADMIN = "admin", "Администратор"

    first_name = models.CharField(max_length=150, blank=True, verbose_name="Имя", help_text="Введите имя")
    last_name = models.CharField(max_length=150, blank=True, verbose_name="Фамилия", help_text="Введите фамилию")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата рождения", help_text="Введите дату рождения")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Номер телефона", help_text="Введите номер телефона")
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите Email")
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    image = models.ImageField(upload_to="users/", blank=True, null=True, verbose_name="Фотография", help_text="Добавьте фотографию")
    address = models.CharField(max_length=300, blank=True, verbose_name="Адрес", help_text="Введите адрес")
    bio = models.TextField(blank=True, verbose_name="О себе", help_text="Расскажите о себе")
    is_student = models.BooleanField(default=False)
    is_active_reader = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        """
        Строковое представление модели пользователя.
        """
        return f"{self.email} ({self.role})"
