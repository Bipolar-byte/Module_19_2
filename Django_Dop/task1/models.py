from django.db import models
from decimal import Decimal


class Buyer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя покупателя")
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Баланс", default=Decimal('0.00'))
    age = models.PositiveIntegerField(verbose_name="Возраст")

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название игры")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    size = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Размер игры (в GB)")
    description = models.TextField(verbose_name="Описание игры")
    age_limited = models.BooleanField(default=False, verbose_name="Ограничение по возрасту 18+")
    buyer = models.ManyToManyField(Buyer, related_name='games', verbose_name="Покупатели")

    def __str__(self):
        return self.title
