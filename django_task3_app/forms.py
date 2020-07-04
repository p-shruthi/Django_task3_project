from django import forms
from .models import user, UserBlog

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('email','password')

class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = UserBlog
        fields = '__all__'
