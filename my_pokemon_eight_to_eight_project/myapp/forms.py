# Подключаем компонент для работы с формой
from django import forms
# Подключаем компонент UserCreationForm
from django.contrib.auth.forms import UserCreationForm
# Подключаем модель User
from django.contrib.auth.models import User
from .models import ProfileDB


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

# Создаём класс формы
class ProfileForm(forms.ModelForm):
    class Meta:
        # Свойство модели User
        model = ProfileDB
        # Свойство назначения полей
        fields = ('user', 'grade_book', 'patronymic', 'date', 'sex', 'characters', 'phone_number', 'img')