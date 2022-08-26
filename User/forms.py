from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=75,
        required=True,
        help_text='Enter your first name',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your first name', 'id': 'first_name'})
    )

    last_name = forms.CharField(
        max_length=75,
        required=True,
        help_text='Enter your last name',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your last name', 'id': 'last_name'})
    )

    username = forms.CharField(
        max_length=75,
        required=True,
        help_text='Enter your username',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your username',  'id': 'username'})
    )

    email = forms.EmailField(
        max_length=75,
        required=True,
        help_text='Enter your email address',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your email', 'id': 'email', 'autocomplete': 'on', })
    )

    password1 = forms.CharField(
        max_length=75,
        required=True,
        help_text='Enter password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your password', 'id': 'password1'})
    )

    password2 = forms.CharField(
        max_length=75,
        required=True,
        help_text='Repeat your password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm your password', 'id': 'password2'})
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',
                  'username', 'password1', 'password2']
