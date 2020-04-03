from django import forms

class fileform(forms.Form):
    
    file=forms.FileField()