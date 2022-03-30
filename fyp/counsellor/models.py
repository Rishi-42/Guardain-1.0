from django.db import models
from django.contrib.auth.models import User
from account.models import CounsellorDetail
from froala_editor.fields import FroalaField
from .healer_blog import *

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    image = models.ImageField(upload_to='counsellor_blog/images/', blank=True, null=True)
    content = FroalaField()

    counsellor_name_id = models.ForeignKey(CounsellorDetail, blank=True , null=True , on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)