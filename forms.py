from django import forms


class myForm(forms.Form):
    tags = forms.CharField(label='tags', max_length=100)
