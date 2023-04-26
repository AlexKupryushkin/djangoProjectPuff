from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


class DivansAddForm(forms.Form):
    """добавление дивана"""
    count = forms.IntegerField(min_value=1, max_value=10, required=True)


class CreateOrderForm(forms.ModelForm):
    """заказ товара"""

    class Meta:
        model = Orders
        fields = ["name", "phone", "address"]


class RegisterUserForm(UserCreationForm):
    """регистрация пользователя"""

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }
