from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets
from django import forms
from products.models import Comment

class UserRegisterForm(UserCreationForm):
    email =forms.EmailField()

    class Meta:
        model =User
        fields =['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields =['body']
        widgets={
            'body':forms.TextInput(attrs={'class': 'form-control'}),
        }