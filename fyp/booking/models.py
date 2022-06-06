from django.db import models
from account.models import Account
from .create_slug import *
# Create your models here.

class Meeting(models.Model):
    meeting_title = models.CharField(max_length=100)
    slug =models.SlugField(max_length=100, unique=True)
    client_age = models.IntegerField()
    marital_status = models.CharField(max_length=100)
    client_details = models.ForeignKey(Account, on_delete=models.CASCADE)
    counsellor_details = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='counsellor_details')
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    # meeting_location = models.CharField(max_length=255)
    meeting_description = models.TextField()
    # meeting_created_by = models.CharField(max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.meeting_title

    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.meeting_title)
        super(Meeting, self).save(*args, **kwargs)