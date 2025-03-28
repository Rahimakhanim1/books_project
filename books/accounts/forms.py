from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control bg-success',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    
class UserForm(UserCreationForm):
    username = forms.CharField(max_length=50,required=True,label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True,label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(required=True, label='Paswword', widget=forms.PasswordInput(attrs={'class':'form-control','name':'password1'}))
    password2 = forms.CharField(required=True, label='Re password', widget=forms.PasswordInput(attrs={'class':'form-control','name':'password2'}))
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password1 = cleaned_data.get("password1")
    #     password2 = cleaned_data.get("password2")

    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords do not match.")

    #     return cleaned_data