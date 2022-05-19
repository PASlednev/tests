from django.db import models
from django.urls import reverse


class Test_group(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название группы')  # Название группы
    description = models.CharField(blank=True, verbose_name='Описание группы', max_length=250)  # Описание группы
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото',
                              blank=True)  # ссылка на фотографию к тесту
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')  # время создания теста


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группы по категориям'
        verbose_name_plural = 'Группы по категориям'
        ordering = ['time_create', 'title']


class Test_title(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название теста')
    questions_count = models.IntegerField(verbose_name='Количество вопросов', default=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')  # Тест опубликован
    test_group = models.ForeignKey(Test_group, on_delete=models.CASCADE, verbose_name='Группа тестов', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тесты по категориям'
        verbose_name_plural = 'Тесты по категориям'
        ordering = ['title']


class Question(models.Model):
    question_text = models.CharField(blank=True, verbose_name='Поле вопроса', max_length=250)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    test_title = models.ForeignKey(Test_title, on_delete=models.CASCADE, verbose_name='Выбор теста', null=True)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Поле вопроса'
        verbose_name_plural = 'Поля вопроса'
        ordering = ['id']


class Answer(models.Model):
    answer_text = models.CharField(max_length=250, verbose_name='Ответ')
    result = models.BooleanField(default=False, verbose_name='Правильный')
    questions = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Поле ответа'
        verbose_name_plural = 'Поля ответа'
        ordering = ['answer_text']

    def get_absolute_url(self):
        return reverse('group_test', kwargs={'group_test_id': self.pk})
