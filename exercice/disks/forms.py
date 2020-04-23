from django import forms


class RechercheForm(forms.Form):
    search = forms.CharField(max_length=100)
