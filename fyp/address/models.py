from django.db import models
from account.models import Account


class Province(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class District(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)
    b_image = models.ImageField(upload_to='images/', blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name



class Adresses(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    ward_no = models.CharField(max_length=30)
    tole = models.CharField(max_length=30)
    user_name = models.ForeignKey(Account, on_delete=models.CASCADE)


    def __str__(self):
        return self.tole
