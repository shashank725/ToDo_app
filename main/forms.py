from django import forms

class CreateNewList(forms.Form):
    name=forms.CharField(label="Name", max_length=100)
    check=forms.BooleanField(required=False)