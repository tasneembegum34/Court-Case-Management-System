from django import forms
from django.forms import fields
from .models import Invoice,LineItem

class InvoiceForm(forms.ModelForm):
    class Meta: 
        model = Invoice
        fields='__all__'
        
class LineItemForm(forms.ModelForm):
    class Meta:
        model= LineItem
        fields='__all__'