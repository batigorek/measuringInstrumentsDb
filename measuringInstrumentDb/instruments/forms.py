from .models import Calipers, Micrometers
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput


class CalipersForm(ModelForm):
    class Meta:
        model = Calipers
        fields = ['inv_number', 'fac_number', 'accuracy', 'meas_limit', 'last_date_check', 'next_date_check', 'checked']

        widgets = {
            "inv_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Инвентарный номер'
            }),
            "fac_number": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заводской номер'
            }),
            "accuracy": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Точность'
            }),
            "meas_limit": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Предел измерения'
            }),
            "last_date_check": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата следующей проверки'
            }),
            "next_date_check": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата следующей проверки'
            }),
            "checked": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия И. О. проверяющего'
            })
        }


class MicrometersForm(ModelForm):
    class Meta:
        model = Micrometers
        fields = ['inv_number', 'fac_number', 'accuracy', 'meas_limit', 'last_date_check', 'next_date_check',
                  'checked']

        widgets = {
            "inv_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Инвентарный номер'
            }),
            "fac_number": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заводской номер'
            }),
            "accuracy": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Точность'
            }),
            "meas_limit": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Предел измерения'
            }),
            "last_date_check": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата следующей проверки'
            }),
            "next_date_check": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата следующей проверки'
            }),
            "checked": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия И. О. проверяющего'
            })
        }
