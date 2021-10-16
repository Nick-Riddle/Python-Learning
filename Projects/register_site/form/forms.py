from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'registration__field-input', 'placeholder': 'Login'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'registration__field-input', 'placeholder': 'Password'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'registration__field-input', 'placeholder': 'Login'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'registration__field-input', 'placeholder': 'Email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'registration__field-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'registration__field-input', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
