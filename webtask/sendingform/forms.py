from .models import Feedback
from django.forms import ModelForm, TextInput, Textarea
from django import forms


# Класс формы отправки отзывов
class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "text", "estimation"]
        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            "text": Textarea(attrs={'class': 'form-control form_text--size', 'placeholder': 'Введите текст отзыва'}),
            "estimation": TextInput(attrs={'class': 'form-control form_estimation--size', 'type': 'number', 'min': '1', 'max': '5', 'placeholder': 'Оценка от 1 до 5'}),
        }


# Класс фильтр отзвывов
class FeedbackFilterForm(forms.Form):
    name = forms.CharField(label='Автор', required=False)
    text = forms.CharField(label='Текст', required=False)
    estimation = forms.IntegerField(label='Оценка', required=False)

    ordering_name = forms.ChoiceField(label='Сортировка по автору', required=False, choices=[
        ["", "-"],
        ["name", "по возрастанию"],
        ["-name", "по убыванию"],
    ])

    ordering_estimation = forms.ChoiceField(label='Сортировка по оценке', required=False, choices=[
        ["", "-"],
        ["estimation", "по возрастанию"],
        ["-estimation", "по убыванию"]
    ])
