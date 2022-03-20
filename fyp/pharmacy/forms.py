from django import forms
from .models import Add_product

class AddProductForm(forms.ModelForm):
    contraindiction = forms.CharField(widget=forms.Textarea(attrs={'rows': '3', 'cols': '50'}))
    indiction = forms.CharField(widget=forms.Textarea(attrs={'rows': '3', 'cols': '50'}))
    special_precautions = forms.CharField(widget=forms.Textarea(attrs={'rows': '3', 'cols': '50'}))
    adverse_effect = forms.CharField(widget=forms.Textarea(attrs={'rows': '3', 'cols': '50'}))



    class Meta:
        model = Add_product
        fields = ('product_name', 'slug', 'image', 'cost', 'stock', 'dose_child', 'dose_adult', 'category', 'contraindiction', 'indiction', 'special_precautions', 'adverse_effect', 'pharmacy_name_id')

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['product_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['cost'].widget.attrs.update({'class': 'form-control'})
        self.fields['stock'].widget.attrs.update({'class': 'form-control'})
        self.fields['dose_child'].widget.attrs.update({'class': 'form-control'})
        self.fields['dose_adult'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['contraindiction'].widget.attrs.update({'class': 'form-control'})
        self.fields['indiction'].widget.attrs.update({'class': 'form-control'})
        self.fields['special_precautions'].widget.attrs.update({'class': 'form-control'})
        self.fields['adverse_effect'].widget.attrs.update({'class': 'form-control'})
