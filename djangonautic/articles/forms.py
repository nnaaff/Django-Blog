# a model for forms for a logged-in User to create and add a new article

from django import forms
from . import models

class CreateArticle(forms.ModelForm):  # inherits from django.forms.ModelForm so can perform validation, etc.
    class Meta:
        model = models.Article
        fields = ['title', 'slug', 'body', 'thumb']

