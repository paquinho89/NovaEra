from django import forms
from django.forms import ModelForm
from artigos.models import artigo_comments, newsletter_email_contratacion


class CommentForm(forms.ModelForm):
    class Meta:
        model=artigo_comments
        fields = ['name', 'email', 'body_comments']
#Esto dos widgets é para meter o formato de bootstrap no form. {{ form }} que está en artigos_content.html.
#O attrs é CSS style
        widgets = {
            'name': forms.TextInput (attrs = {'class': 'form-control'}),
            'email': forms.TextInput (attrs = {'class': 'form-control'}),
            'body_comments': forms.Textarea (attrs = {'class': 'form-control'})
        }


class newsletter_contratacion_form(forms.ModelForm)   :
    class Meta:
        model = newsletter_email_contratacion
        fields = ['email_subscriber']
        widgets = {
            'email_subscriber': forms.EmailInput (attrs = {'class': 'form-control', 'placeholder':'Ex: "pepe@hotmail.com"'})
        }


        