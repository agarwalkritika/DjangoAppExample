from django import forms
from .models import CustomUser


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput, required=True)
    otp = forms.CharField(widget=forms.PasswordInput, max_length=6, required=False)


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number','email_id','gender']


class SearchBar(forms.Form):
    search_string = forms.CharField(required=True)

