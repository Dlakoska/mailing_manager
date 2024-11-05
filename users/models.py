from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=100, verbose_name='Токен', null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
