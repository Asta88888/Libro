from django.db import models

class Author(models.Model):
    """
    Модель автора книги.
    """
    first_name = models.CharField(max_length=200, verbose_name="Имя", help_text="Введите имя", blank=True, null=True)
    last_name = models.CharField(max_length=200, verbose_name="Фамилия", help_text="Введите фамилию", blank=True, null=True)
    middle_name = models.CharField(max_length=200, verbose_name="Отчество", help_text="Введите отчество", blank=True, null=True)
    bio = models.TextField(verbose_name="Описание", help_text="Введите описание")
    years_of_life = models.CharField(max_length=50, verbose_name="Годы жизни", help_text="Введите годы жизни")
    image = models.ImageField(upload_to="authors/", verbose_name="Фото", help_text="Добавьте фотографию")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["last_name"]

    def __str__(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip()

class Genre(models.Model):
    """
    Модель жанров книги.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Жанр", help_text="Введите жанр книги")
    description = models.TextField(verbose_name="Описание", help_text="Введите описание")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Модель книги.
    """
    title = models.CharField(max_length=300, verbose_name="Название", help_text="Введите название книги")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", verbose_name="Автор")
    genres = models.ManyToManyField(Genre, related_name="books", verbose_name="Жанры")
    description = models.TextField(verbose_name="Описание", help_text="Введите описание")
    publish_date = models.DateField(null=True, blank=True, verbose_name="Дата публикации", help_text="Введите дату публикации")
    cover = models.ImageField(upload_to="books/")
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["title"]

    def __str__(self):
        return self.title
