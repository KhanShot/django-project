from bonus_pro3.settings import AUTH_USER_MODEL
from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Tours, FormFeedbacks
from django.contrib.auth import get_user_model




class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input', 'id':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-input', 'id':'password'}))


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input', 'id':'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-input', 'id':'pass'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-input', 'id':'word'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-input', 'id':'email'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-input', 'id':'age'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input', 'id':'name'}))

    class Meta:

        model = User
        fields = ('username', 'email', 'password1', 'password2', 'age', 'name')

class ManagersCreateForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'pass'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'pass'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'id':'email'}))

    CHOICES= (('manager', 'manager'),
        ('client', 'client'),
        ('admin', 'admin'),)
    user_type = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class':'form-control', 'id':'user_type'}))

    class Meta:

        model = User
        fields = ('username', 'email', 'password1','password2','user_type')


class ToursCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'username'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'description'}))
    price = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control', 'id':'price'}))
    date = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'date'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control', 'id':'image'}))
    class Meta:
        model = Tours
        fields = ('name', "description" ,'price' ,'date','image')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Tours
        fields = ['image']


class FeedbackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input', 'id':'name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-input', 'id':'email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input', 'id':'phone'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input', 'id':'message'}))

    class Meta:
        model = FormFeedbacks