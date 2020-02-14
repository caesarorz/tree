from django import forms

from .models import Tree, TreeImage

class TreeImageForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = ('user', 'title', 'description', 'location')