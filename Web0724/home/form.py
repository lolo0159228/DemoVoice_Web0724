from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'帳號/電子郵件'}))
    password = forms.CharField(max_length=12,widget=forms.PasswordInput)