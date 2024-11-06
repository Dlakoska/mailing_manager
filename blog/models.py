from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок",
                             help_text="Введите название продукта")
    description = models.TextField(
        verbose_name="Содержимое", help_text="Введите содержимое блога"
    )
    image = models.ImageField(
        upload_to="images/",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите изображение",
    )
    created_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата создания(записи в БД)")
    views_count = models.IntegerField(default=0, verbose_name="количество просмотров")
    owner = models.ForeignKey(User, verbose_name='Владелец блога', on_delete=models.CASCADE, **NULLABLE)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title", "-created_at"]

    def __str__(self):
        return self.title
