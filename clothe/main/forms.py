from django import forms
from .admin import UserCreationForm
from .models import User

class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'gender', 'username', 'password1', 'password2')