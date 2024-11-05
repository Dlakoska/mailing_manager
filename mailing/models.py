from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='Email адрес', unique=True)
    full_name = models.CharField(max_length=150, verbose_name='Ф.И.О. клиента')
    сomment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    owner = models.ForeignKey(User, verbose_name='Владелец записи о клиенте', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=100, verbose_name='Тема письма')
    message = models.TextField(verbose_name='Сообщение')
    owner = models.ForeignKey(User, verbose_name='Владелец сообщения', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class Mailing(models.Model):
    STATUS_CHOICES = [
        ("created", "Создана"),
        ("started", "Активна"),
        ("completed", "Завершена"),
    ]

    PERIODICITY_CHOICES = [
        ("daily", "Ежедневно"),
        ("weekly", "Еженедельно"),
        ("monthly", "Ежемесячно"),
    ]

    description = models.TextField(verbose_name='Описание', **NULLABLE)
    start_time = models.DateTimeField(verbose_name='Дата начала рассылки')
    periodicity = models.CharField(max_length=10, verbose_name='Периодичность', choices=PERIODICITY_CHOICES)
    status = models.CharField(max_length=10, verbose_name='Статус', choices=STATUS_CHOICES, default='created')
    message = models.ForeignKey(Message, verbose_name='Сообщение', on_delete=models.CASCADE)
    client = models.ManyToManyField(Client, verbose_name='Клиенты')
    actual_end_time = models.DateTimeField(verbose_name='Дата завершения рассылки', **NULLABLE)
    owner = models.ForeignKey(User, verbose_name='Владелец рассылки', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        permissions = [('can_edit_status', 'Can edit status')]

class MailingAttempt(models.Model):
    STATUS_CHOICES = [('success', 'Успешно'), ('failed', 'Не успешно')]

    mailing = models.ForeignKey(Mailing, verbose_name='Рассылка', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    server_response = models.TextField(verbose_name='Ответ почтового сервиса', **NULLABLE)
    send_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Попытка {self.id} для рассылки {self.mailing.id}'

    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'
