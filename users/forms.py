from mailing.forms import StyleFormMixin
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django import forms


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)
