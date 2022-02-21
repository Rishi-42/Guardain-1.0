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
        email = self.cleaned_data.get('email')
        try:
            Account.objects.get(email=email)
            raise forms.ValidationError(
                'Email already exists'
            )
        except Account.DoesNotExist:
            pass

    def __init__(self, *args, **kargs):
        super(RegistrationForm, self).__init__(*args, **kargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'example@domain.com'})
        self.fields['term'].widget.attrs.update({'id': 'term_cond'})
        self.fields['user_type'].widget.attrs.update({'class': 'form-control'})
        
class RegistrationFormPharmacy(forms.ModelForm):
    Time_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),


    	]
    work_start = forms.ChoiceField(
        required=True,
        choices=Time_CHOICES,
    )
    work_end = forms.ChoiceField(
        required=True,
        choices=Time_CHOICES,
    )

    class Meta:
        model = PharmacistDetail
        fields = ('phone_no', 'registration_no', 'pharmacy_name', 'pharmacy_email', 'registered_doc', 'profile_image', 'work_start', 'work_end', 'description')

    def __init__(self, *args, **kargs):
        super(RegistrationFormPharmacy, self).__init__(*args, **kargs)
        self.fields['phone_no'].widget.attrs.update({'class': 'form-control', 'placeholder': ' name'})
        self.fields['registration_no'].widget.attrs.update({'class': 'form-control', 'placeholder': ' '})
        self.fields['pharmacy_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pharmacy Name'})
        self.fields['pharmacy_email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'example@domain.com'})
        self.fields['registered_doc'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Pharmacy Registered Document'})
        self.fields['profile_image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'select profile image'})
        # self.fields['district'].widget.attrs.update({'class': 'form-control', 'placeholder': ' name'})
        # self.fields['city'].widget.attrs.update({'class': 'form-control', 'placeholder': ' name'})
        # self.fields['ward'].widget.attrs.update({'class': 'form-control', 'placeholder': ' name'})
        # self.fields['tole'].widget.attrs.update({'class': 'form-control', 'placeholder': ' name'})
        self.fields['work_start'].widget.attrs.update({'class': 'form-control'})
        self.fields['work_end'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write something about your pharmacy here'})
        # self.fields['province_no'].widget.attrs.update({'class': 'form-control'})
        # self.fields['working_days'].widget.attrs.update({'class': 'btn btn-light'})