from django import forms
from django.core.exceptions import ValidationError

from .models import Category, ContactSent


class CategoryForm(forms.ModelForm):

    # name = forms.CharField(label='Имя', initial='Базовая категория')
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя'
    }))

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise ValidationError('Название категории не может быть меньше 3 символов')
        return name

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        if name == 'XXX':
            raise ValidationError('Вы перепутали сайт')

    class Meta:
        fields = ('name', 'img')
        model = Category


# FormView
class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))


class ContactSendForm(forms.ModelForm):
    class Meta:
        model = ContactSent
        fields = '__all__'