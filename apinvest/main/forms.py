# main/forms.py

from django import forms

class InvestorSearchForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    attachment = forms.FileField(required=False, label='Приложение')
