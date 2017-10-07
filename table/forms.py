from django import forms
from .models import Rserv

class RservForm(forms.ModelForm):
    class Meta:
        model= Rserv
        fields= ('rserv_er', 'rserv_call',)
