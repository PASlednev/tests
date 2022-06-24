from django import forms

from .models import *


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'result', 'question']
        widgets = {
            'answer_text': forms.TextInput()
        }
