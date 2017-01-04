from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
        #print (forms)
        email=forms.EmailField(label="email1",required=True)
        passwrd=forms.CharField(label="pass1")

class CodeForms(forms.Form):
    code_data=forms.CharField(label="code")
    

