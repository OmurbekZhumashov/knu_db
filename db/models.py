from django.db import models


# Create your models here.
class Facult(models.Model):
    name = models.CharField(max_length=100, verbose_name="Факультет")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Status(models.Model):
    name = models.CharField(max_length=120, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'


class Obshaga(models.Model):
    name = models.CharField(max_length=25, verbose_name='Общежитие')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Общежитие'
        verbose_name_plural = 'Общежитии'


class People(models.Model):
    obshaga = models.ForeignKey(Obshaga, verbose_name='Общежитие', on_delete=models.CASCADE)
    komnata = models.IntegerField(verbose_name='Комната', db_index=True)
    fio = models.CharField(max_length=150, verbose_name='ФИО', unique=True)
    birthday = models.DateField(verbose_name='Дата рождения', )
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус', )
    facult = models.ForeignKey(Facult, on_delete=models.CASCADE, verbose_name='Факультет', )
    zahislenie = models.DateTimeField(verbose_name='Зачисление', )
    uhod = models.DateTimeField(verbose_name='Уход', )
    image = models.ImageField(verbose_name='Фото', )

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Жители'
        verbose_name_plural = 'Жители'


class Tip(models.Model):
    name = models.CharField(max_length=25, verbose_name='Тип документа')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Тип документа'


class Document(models.Model):
    people = models.ForeignKey(People, verbose_name='Житель', on_delete=models.CASCADE)
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE, verbose_name='Тип документа')
    date = models.DateField(verbose_name='дата приема', auto_now_add=True)
    file = models.FileField(verbose_name='Документ', )

    def __str__(self):
        return str(self.people)

    class Meta:
        verbose_name = 'Перечень документов'
        verbose_name_plural = 'Перечень документов'
