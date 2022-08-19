# accounts/forms.py -->
from django import forms

class NameForm(forms.Form):
    item_name = forms.CharField(label='Item name', max_length=100)