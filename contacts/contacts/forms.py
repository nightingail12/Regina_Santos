from django import forms
from contacts.models import crudst

class contact_form(forms.ModelForm):
    class Meta:
        model = crudst
        fields = "__all__"
