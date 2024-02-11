from django import forms
from django.contrib.auth.models import User
from .models import Profile, Messages
from django.contrib.auth.forms import UserCreationForm


class UserRegForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Name'
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='Email')
    username = forms.CharField(required=True,
                               label='Name')

    class Meta:
        model = User
        fields = ['email', 'username']


class ProfileUpdateForm(forms.ModelForm):
    CHOICES = (('undefined', 'undefined'), ('male', 'Male'), ('female', 'Female'), ('other', 'Other'))

    img = forms.ImageField(required=False,
                           label='Photo',
                           widget=forms.FileInput)
    sex = forms.ChoiceField(required=False,
                            choices=CHOICES,
                            label='Gender')
    send_email = forms.BooleanField(required=False,
                                    label="Receive Email")

    class Meta:
        model = Profile
        fields = ['sex', 'img', 'send_email']


class MessageForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            label='Topic')
    sender = forms.EmailField(required=True,
                             label='Email')
    text = forms.CharField(required=True,
                           label='Text',
                           widget=forms.Textarea())

    class Meta:
        model = Messages
        fields = ['title', 'sender', 'text']
