import datetime

from django.db import models


# Create your models here.


class Instruments(models.Model):
    title = models.CharField('Название', max_length=50, default='')
    anons = models.CharField('Описание', max_length=250, default='')
    count = models.IntegerField('Количество на предприятии')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'


class Calipers(models.Model):
    inv_number = models.CharField('Инвентарный номер', max_length=6)
    fac_number = models.IntegerField('Заводской номер')
    accuracy = models.CharField('Точность', max_length=50, default='')
    meas_limit = models.CharField('Предел измерения', max_length=100, default='')
    last_date_check = models.DateTimeField('Дата последней проверки')
    next_date_check = models.DateTimeField('Дата следующей проверки')
    checked = models.CharField('Фамилия И.О. проверяющего', max_length=100, default='')

    def __str__(self):
        return self.inv_number

    def get_absolute_url(self):
        return f'/instruments/calipers'

    class Meta:
        verbose_name = 'Штангенциркуль'
        verbose_name_plural = 'Штангенциркули'

class Micrometers(models.Model):
    inv_number = models.CharField('Инвентарный номер', max_length=6)
    fac_number = models.IntegerField('Заводской номер')
    accuracy = models.CharField('Точность', max_length=50, default='')
    meas_limit = models.CharField('Предел измерения', max_length=100, default='')
    last_date_check = models.DateTimeField('Дата последней проверки')
    next_date_check = models.DateTimeField('Дата следующей проверки')
    checked = models.CharField('Фамилия И.О. проверяющего', max_length=100, default='')

    def __str__(self):
        return self.inv_number

    def get_absolute_url(self):
        return f'/instruments/calipers'

    class Meta:
        verbose_name = 'Микрометр'
        verbose_name_plural = 'Микрометры'
