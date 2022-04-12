from django import forms
from .models import Meeting


class Schedule_Meeting(forms.ModelForm):
    MARITAL_CHOICES = [
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
        ('divorced', 'Divorced'),
        ('single', 'Single'),
    ]
    marital_status = forms.ChoiceField(
    required=True,
    choices=MARITAL_CHOICES,
    )
    meeting_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control',
        }))
    meeting_time = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time',
        'class': 'form-control',
    }))
    class Meta:
        model = Meeting
        fields = ('meeting_title', 'client_age', 'marital_status', 'client_details', 'meeting_date', 'meeting_time',
                  'meeting_location', 'meeting_description', 'meeting_created_by')

    def __init__(self, *args, **kwargs):
        super(Schedule_Meeting, self).__init__(*args, **kwargs)
        self.fields['meeting_title'].widget.attrs.update({'class': 'form-control'})
        self.fields['client_age'].widget.attrs.update({'class': 'form-control'})
        self.fields['marital_status'].widget.attrs.update({'class': 'form-control'})
        self.fields['client_details'].widget.attrs.update({'class': 'form-control'})
        self.fields['meeting_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['meeting_description'].widget.attrs.update({'class': 'form-control'})
        self.fields['meeting_created_by'].widget.attrs.update({'class': 'form-control'})
