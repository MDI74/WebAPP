from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Модель отзывов
class Feedback(models.Model):
    name = models.CharField('Имя', max_length=30)
    text = models.TextField('Текст', max_length=5000)
    estimation = models.IntegerField('Оценка', validators=[MinValueValidator(1), MaxValueValidator(5)])

    #Внутренний класс в котором определяется такие вещи как разрешения, имя базы данных, абстрация и т.д. Является необязательным
    class Meta:
        verbose_name = 'Отзыв'  # Название в ед.ч
        verbose_name_plural = 'Отзывы'  # Название во мн.ч

    #Метод который используется для отображения объекта на сайте
    def __str__(self):
        return '%s %s' % (self.name, self.estimation)  #Возвращает заданный объект


