from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['category', 'description','difficulty', 'answer']


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

    
# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('name', 'email')

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match.')
#         return cd['password2']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
