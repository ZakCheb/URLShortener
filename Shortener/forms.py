from django import forms
from .models import *

class InputNewUrl(forms.ModelForm):
    class Meta:
        model= ShortURL
        fields = ['original']