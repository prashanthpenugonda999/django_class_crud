from django import forms
from testapp1.models import student



class Std_Form(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"


    
        