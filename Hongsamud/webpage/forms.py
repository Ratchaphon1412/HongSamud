from django import forms
from webpage.models import CATEGORY, GENRES

# class AddBookform(forms.Form):
#     name = forms.CharField(label="Book Name", widget=forms.TextInput(attrs={'autocomplete': 'off'}))
#     author = forms.CharField(label="Author", widget=forms.TextInput(attrs={'list': 'author-list', 'autocomplete': 'off'}))
#     publisher = forms.CharField(label="Publisher", widget=forms.TextInput(attrs={'list': 'publisher-list', 'autocomplete': 'off'}))
#     category = forms.ChoiceField(choices=CATEGORY, label="Category")
#     genre = forms.ChoiceField(choices=GENRES,label="Genre")
#     quantity = forms.IntegerField(min_value=0, label="Quantity")
#     description = forms.CharField(label="Description", required=False)
#     image = forms.CharField(label="Image Link", widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    