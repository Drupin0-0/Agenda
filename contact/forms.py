from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escreva aqui'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escreva aqui'
        })
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escreva aqui'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escreva aqui'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escreva aqui'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['picture'].widget.attrs.update({
            'class': 'form-control-file',
        })

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        )

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name and last_name and first_name == last_name:
            msg = ValidationError('Primeiro nome não pode ser igual ao segundo', code='invalid')
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return cleaned_data

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            raise ValidationError('Não digite ABC nesse campo', code='invalid')
        return first_name


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, min_length=3)
    last_name = forms.CharField(required=True, min_length=3)
    email = forms.EmailField(required=True, min_length=3)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Já existe este email cadastrado', code='invalid')
        return email


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
