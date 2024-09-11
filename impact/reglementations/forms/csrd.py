from django import forms

from reglementations.models.csrd import RapportCSRD


class RapportPersonnelCSRDForm(forms.ModelForm):
    class Meta:
        model = RapportCSRD
        fields = ["habilitation", "annee", "description"]


class RapportOfficielCSRDForm(forms.ModelForm):
    class Meta:
        model = RapportCSRD
        fields = ["entreprise", "annee", "description"]
