from django.db import models
from account.models import PharmacistDetail

class Add_product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null = True, blank = True)
    image = models.ImageField(upload_to='photos/product_images')
    cost = models.IntegerField()
    stock = models.IntegerField()
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


class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null = True, blank = True)

    # auto
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name
