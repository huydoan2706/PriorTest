from django import forms
from django.utils import timezone


class CreateNewReceipt(forms.Form):
    receipt_date = forms.DateField(label="Receipt Date", required=False)
    supplier_name = forms.CharField(label="Supplier Name", max_length=255)
