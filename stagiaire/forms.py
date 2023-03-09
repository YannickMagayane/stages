from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Filiaire


class UserForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nom Utilisateur',
                "class": "form-control"
            }
        )
    )
    first_name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Prenom',
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Post nom',
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        label='',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Mot de passe',
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmer mot de passe',
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['promotion', 'photo', 'option', 'sex',  'end_stage']

        widgets = {
            'promotion':forms.TextInput(attrs={'class':'form-control'}),
            'photo' : forms.FileInput(attrs={'class':'form-control'}),
            'option':forms.Select(attrs={'class':'form-control'}),
            'sex':forms.Select(attrs={'class':'form-control'}),
            'end_stage':forms.DateTimeInput(attrs={'class':'form-control'}),

        }


class FiliaireForm(forms.ModelForm):
    class Meta:
        model = Filiaire
        fields = '__all__'
