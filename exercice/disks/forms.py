from django import forms


class RechercheForm(forms.Form):
    truc_cherche = forms.CharField(max_length=100)
