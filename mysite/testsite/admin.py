from django.contrib import admin

from .models import *


class Test_groupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create',)


class Test_titleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text')
    list_display_links = ('id', 'question_text')


admin.site.register(Test_group, Test_groupAdmin)
admin.site.register(Test_title, Test_titleAdmin)
admin.site.register(Question, QuestionAdmin)
