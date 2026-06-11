from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Autor, Editora, Livro, Publica
from django.utils.translation import gettext_lazy as _


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, 
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'email@exemplo.com', 
                                 'class': 'input-text'
                                 }))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Este email já está em uso.')
        return email

class SignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input-text'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input-text'})
    )

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
        }


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
        }


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro

        fields = ['isbn', 'titulo', 'publicacao', 'preco', 'estoque', 'editora']

        labels = {
            'isbn': _('ISBN'),
            'titulo': _('Título'),
            'publicacao': _('Data de Publicação'),
            'preco': _('Preço'),
            'estoque': _('Estoque'),
            'editora': _('Editora'),
        }

        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'publicacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'editora': forms.Select(attrs={'class': 'form-control'}),
        }


class PublicaForm(forms.ModelForm):
    class Meta:
        model = Publica
        fields = ['livro', 'autor']
        widgets = {
            'livro': forms.Select(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
        }