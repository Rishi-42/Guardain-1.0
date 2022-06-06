from django import forms
from .models import UploadPrescription

class UploadPrescriptionForm(forms.ModelForm):

    class Meta:
        model = UploadPrescription
        fields = ('name', 'age', 'prescription', 'prescripted_by', 'prescripted_for')

    def __init__(self, *args, **kargs):
        super(UploadPrescriptionForm, self).__init__(*args, **kargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'name'})
        self.fields['age'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'age'})
        self.fields['prescription'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'prescription'})
        self.fields['prescripted_by'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'prescripted_by'})
        self.fields['prescripted_for'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'prescripted_for'})

