from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.ChoiceField(label='Search Word')