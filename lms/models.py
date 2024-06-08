from django.db import models


class Course(models.Model):
    """Курс"""
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='courses/', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return f'Курс {self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """Урок"""
    title = models.CharField(max_length=100, verbose_name='Название')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='lessons/', null=True, blank=True, verbose_name='Изображение')
    link = models.URLField(verbose_name='Ссылка на видео-урок')

    def __str__(self):
        return f'Урок {self.title} из курса:{self.course}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
