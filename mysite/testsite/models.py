from django.db import models


class test_title(models.Model):
    title = models.CharField(max_length=300)  # Название теста
    description = models.TextField(blank=True)  # Описание теста
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")  # ссылка на фотографию к тесту
    time_create = models.DateTimeField(auto_now_add=True)  # время создания теста
    is_published = models.BooleanField(default=True)  # поле опубликовано
