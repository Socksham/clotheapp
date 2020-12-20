from django import forms
from django.contrib.postgres import fields
from .admin import UserCreationForm
from .models import *

class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'gender', 'username', 'password1', 'password2')

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'content'}))
    class Meta:
        model = Post
        fields = ('content', 'image')