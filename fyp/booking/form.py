from django import forms
from .models import Meeting
from datetime import date
from dateutil.relativedelta import relativedelta

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
    today_date = date.today()
    future_date = today_date + relativedelta(months=1)
    meeting_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control',
        'min': today_date,
        'max': future_date,
        }))
    meeting_time = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time',
        'class': 'form-control',
        'min': '09:00',
        'max':'16:00',
    }))
    class Meta:
        model = Meeting
        fields = ('meeting_title', 'client_age', 'marital_status', 'meeting_date', 'meeting_time',
                  'meeting_description')

    def __init__(self, *args, **kwargs):
        super(Schedule_Meeting, self).__init__(*args, **kwargs)
        self.fields['meeting_title'].widget.attrs.update({'class': 'form-control'})
        self.fields['client_age'].widget.attrs.update({'class': 'form-control'})
        self.fields['marital_status'].widget.attrs.update({'class': 'form-control'})
        # self.fields['meeting_location'].widget.attrs.update({'class': 'form-control'})
        self.fields['meeting_description'].widget.attrs.update({'class': 'form-control'})
        # self.fields['meeting_created_by'].widget.attrs.update({'class': 'form-control'})
