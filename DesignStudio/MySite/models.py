from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    name = models.CharField(max_length=250, verbose_name="ФИО", help_text="Только кириллические буквы, дефис и пробелы")
    username = models.CharField(max_length=35, verbose_name="Логин", unique=True,
                                help_text="Только латиница и дефис, уникальный")
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Согласен с обработкой '
                                                    'персональных данных?')


class Meta(AbstractUser.Meta):
    pass


class Category(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите категорию")

    def __str__(self):
        return self.name


class Applications(models.Model):
    title = models.CharField(max_length=100)
    deck = models.TextField(max_length=1000, default='something')
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title
