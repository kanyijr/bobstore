from django import forms
from django.contrib.auth.models import User
from .models import Buyer
from django.contrib.auth.forms import UserCreationForm


class loginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    

class signupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password' ]   
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'

            }),

            'password':forms.PasswordInput(attrs={
                'class':'form-control'
            })

      
        }     

class signupfinalForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = '__all__'
        exclude= ['user']

        widgets = {

            'firstname': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'lastname':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control'
            })

        }
        