from django.utils.text import slugify 

import string
import random


def generate_random_string(N): 
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    return res
  

def generate_slug(text):
    new_slug = slugify(text)
    from .models import PharmacistDetail
    
    if PharmacistDetail.objects.filter(slug = new_slug).first():
        # since the product name must be unique the slug is also unique so no need to add random strings
        # return generate_slug(text)
        return generate_slug(text + generate_random_string(3))
    return new_slug