from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

# class UserRegForm(forms.Form):


class UserRegForm(UserCreationForm):

    username = forms.CharField(
        label='Nickname:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nickname'})
    )
    email = forms.EmailField(
        label='Email:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password1 = forms.CharField(
        label='Password:',
        required=True,
        help_text='Numbers, letters and special symbols',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your password'})
    )
    password2 = forms.CharField(
        label='Your password:',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdaterForm(forms.ModelForm):
    username = forms.CharField(
        label='Nickname:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nickname'})
    )
    email = forms.EmailField(
        label='Email:',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Update photo',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']
