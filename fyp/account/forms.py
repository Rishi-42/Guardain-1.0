from django import forms
from .models import Account, PharmacistDetail


class RegistrationForm(forms.ModelForm):
    USER_TYPE_CHOICES = [
    ('customer', 'Customer'),
    ('pharmacist', 'Pharmacist'),
    ('counsellor', 'Counsellor'),
    	]

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }), min_length=8)

    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))

    term = forms.BooleanField(required=True)
    user_type = forms.ChoiceField(
        required=True,
        choices=USER_TYPE_CHOICES,
    )

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'password', 'user_type')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                'Password did not match'
            )
    
    def __init__(self, *args, **kargs):
        super(RegistrationForm, self).__init__(*args, **kargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'example@domain.com'})
        self.fields['term'].widget.attrs.update({'id': 'term_cond'})
        self.fields['user_type'].widget.attrs.update({'class': 'form-control'})
        


class RegistrationFormPharmacy(forms.ModelForm):
    USER_TYPE_CHOICES = [
        ('customer', 'Customer'),
        ('pharmacist', 'Pharmacist'),
        ('counsellor', 'Counsellor'),
    	]
    user_type = forms.ChoiceField(
        required=True,
        choices=USER_TYPE_CHOICES,
    )

    class Meta:
        model = PharmacistDetail
        fields = ('phone_no', 'ogrn_number', 'inn_number', 'licence', 'pharmacy_name', 'telephone', 'pharmacy_email', 'estd_date', 'registered_doc', 'profile_image', 
        'working_days', 'working_hours_start', 'working_hour_end', 'description')

    
    def __init__(self, *args, **kargs):
        super(RegistrationFormPharmacy, self).__init__(*args, **kargs)
        self.fields['phone_no'].widget.attrs.update({'class': 'form-control', 'placeholder': ' name'})
        self.fields['ogrn_number'].widget.attrs.update({'class': 'form-control', 'placeholder': ' name'})
        self.fields['inn_number'].widget.attrs.update({'class': 'form-control', 'placeholder': ' '})
        self.fields['licence'].widget.attrs.update({'class': 'form-control', 'placeholder': ' '})
        self.fields['pharmacy_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pharmacy Name'})
        self.fields['telephone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Telephone number'})
        self.fields['pharmacy_email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'example@domain.com'})
        self.fields['estd_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['registered_doc'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pharmacy Registered Document'})
        self.fields['profile_image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'select profile image'})
        self.fields['working_days'].widget.attrs.update({'class': 'form-control'})
        self.fields['working_hours_start'].widget.attrs.update({'class': 'form-control'})
        self.fields['working_hour_end'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write something here'})

        self.fields['user_type'].widget.attrs.update({'class': 'form-control'})


