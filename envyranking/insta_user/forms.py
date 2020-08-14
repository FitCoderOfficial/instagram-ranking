from django import forms
from .models import insta_user_Data


class PostForm(forms.ModelForm):
    class Meta:
        model = insta_user_Data
        fields = ['username']
