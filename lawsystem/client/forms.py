from django import forms
from django.forms import fields
from.models  import sectionNoDetails

class sectionNoDetailsForm(forms.ModelForm):
    class Meta: 
        model = sectionNoDetails
        fields='__all__'
        
 