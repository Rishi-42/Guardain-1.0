from django.db import models
from account.models import PharmacistDetail
from .healer import *
from django.urls import reverse

class Add_product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null = True, blank = True)
    image = models.ImageField(upload_to='photos/product_images')
    cost = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    dose_child = models.CharField(max_length=200)
    dose_adult = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    contraindiction = models.CharField(max_length=500)
    indiction = models.CharField(max_length=500)
    special_precautions = models.CharField(max_length=500)
    adverse_effect = models.CharField(max_length=500)
    pharmacy_name_id = models.ForeignKey(PharmacistDetail, on_delete=models.CASCADE)

    # auto
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.product_name)
        super(Add_product, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('product_detail', args=[self.pharmacy_name_id.id ,self.category.slug, self.slug])

class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null = True, blank = True)

    # auto
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


