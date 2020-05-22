from django import forms
from .import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'desc']

class UploadFileForm(forms.Form):
    file = forms.FileField()