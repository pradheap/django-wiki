from django import forms as forms

from models import Page


class PageForm(forms.Form):
    name = forms.CharField(max_length=255)
    title = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea())

    def clean_name(self):
        return self.cleaned_data['name']

    def clean_title(self):
        return self.cleaned_data['title']
