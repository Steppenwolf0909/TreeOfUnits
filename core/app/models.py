from django.db import models

class Employee(models.Model):
    fio = models.CharField(max_length=200, verbose_name='ФИО')
    position = models.CharField(max_length=200, verbose_name='Должность')
    date_coming = models.DateField(verbose_name='Дата приема на работу')
    salary = models.IntegerField(default=0)
    subdivision = models.ForeignKey('Subdivision', on_delete=models.CASCADE, verbose_name='Подразделение',
                                        blank=True, null=True)

    def __str__(self):
        return f'{self.position} {self.fio}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Subdivision(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наимаенование')
    parent_subdivision = models.ForeignKey('Subdivision', on_delete=models.CASCADE, verbose_name='Выше стоящие подразделение',
                                        blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'