from django import forms

from .models import *


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', ' test_title']
