from django import forms
from .models import Inquiry

class InquiryCreationForm(forms.ModelForm):
    class Meta:
        model=Inquiry
        fields=['name', 'email', 'context']