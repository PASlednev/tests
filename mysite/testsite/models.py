from django.db import models
from django.urls import reverse


class test_title(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заголовок')  # Название теста
    description = models.TextField(blank=True, verbose_name='Описание теста')  # Описание теста
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')  # ссылка на фотографию к тесту
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')  # время создания теста
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')  # поле опубликовано

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тесты по категориям'
        verbose_name_plural = 'Тесты по категориям'
        ordering = ['time_create', 'title']

    def get_absolute_url(self):
        return reverse('group_test', kwargs={'group_test_id': self.pk})
