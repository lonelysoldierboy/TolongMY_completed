from django import forms
from .models import victim

class VictimForm(forms.ModelForm):
   class Meta:
        model = victim
        fields = ['name', 'ic', 'number']