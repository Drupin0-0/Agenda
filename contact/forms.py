from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    def __init__(self,  *args, **kwargs):
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
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category'
            
            
            )
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva aqui'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva aqui'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva aqui'}),
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError('Primeiro nome não pode ser igual ao segundo', code='invalid')
            
            
            self.add_error(
                'first_name', msg
            )
            self.add_error(
                'last_name', msg
            )


        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Nao digite ABC nesse campo',
                    code='invalid'
            )
        )
        return first_name
    
    
        