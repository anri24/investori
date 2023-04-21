from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib import messages
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    firstname = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    lastname = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    piradinomeri = forms.CharField(
        widget= forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    telefonis_nomeri = forms.CharField(
        widget= forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    dabadebis_dge = forms.CharField(
        widget= forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    dabadebis_tve = forms.CharField(
        widget= forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    dabadebis_weli = forms.CharField(
        widget= forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    qveyana = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    qalaqi = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','firstname','lastname','piradinomeri','telefonis_nomeri','dabadebis_dge','dabadebis_tve','dabadebis_weli','qveyana','qalaqi')
        


class CategoryForm(forms.Form):
    categories = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )


  
class ProductForm(forms.ModelForm):
  
    class Meta:
        model = Product
        fields = ['category', 'sub_category','photo','qonebisTipiHouse','price','description']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('full_name','comment')

        widgets ={
            'full_name': forms.TextInput(attrs={'class': 'form-control','style':'width:300px;'}),
            'comment': forms.Textarea(attrs={'class': 'form-control','style':'font-size:15px'}),
}