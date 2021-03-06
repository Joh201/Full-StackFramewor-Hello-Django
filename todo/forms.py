from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # associates the form with its model and info about itself
    class Meta:
        model = Item
        # these are fields to display to the user
        fields = ['name', 'done']

