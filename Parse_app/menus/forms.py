from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class AccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

class UserLoginForm(AuthenticationForm):
    pass

