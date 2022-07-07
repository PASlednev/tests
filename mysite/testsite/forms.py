from django import forms

from .models import *


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['result', 'question']
        widgets = {
            'answer_text': forms.TextInput()
        }
