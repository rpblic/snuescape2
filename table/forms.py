from django import forms
from .models import Rserv

class PostForm(forms.ModelForm):
    class Meta:
        model= Rserv
        fields= ('rserv_date', 'rserv_er', 'rserv_call', 'applied',)
