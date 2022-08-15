from django.db import models


class Answer(models.Model):
    answer_text = models.CharField(max_length=250, verbose_name='Ответ')
    result = models.BooleanField(default=False, verbose_name='Правильный')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True, verbose_name='Вопрос')
    # добавить связь на модель User, чтобы понимать кто передал ответ.

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Поле ответа'
        verbose_name_plural = 'Поля ответа'
        ordering = ['answer_text']


class Question(models.Model):
    question_text = models.CharField(blank=True, verbose_name='Поле вопроса', max_length=250)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    test_title = models.ForeignKey('Test_title', on_delete=models.CASCADE, null=True, verbose_name='название теста')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Поле вопроса'
        verbose_name_plural = 'Поля вопроса'
        ordering = ['id']

    # def get_absolute_url(self):
    #     return reverse('questions', kwargs={'question_id': self.pk})


class Test_title(models.Model):
    title_test = models.CharField(max_length=300, verbose_name='Название теста')
    questions_count = models.IntegerField(verbose_name='Количество вопросов', default=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')  # Тест опубликован
    tests = models.ForeignKey('Test_group', on_delete=models.CASCADE, verbose_name='Название группы тестов',
                              null=True)

    def __str__(self):
        return self.title_test

    class Meta:
        verbose_name = 'Тесты по категориям'
        verbose_name_plural = 'Тесты по категориям'
        ordering = ['title_test']

    # def get_absolute_url(self):
    #     return reverse('tests', kwargs={'test_id': self.pk})


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

    # def get_absolute_url(self):
    #     return reverse('test_group', kwargs={'test_group_id': self.pk})
