from django.db import models
from account.models import PharmacistDetail


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
    b_image = models.ImageField(upload_to='images/', blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Adresses(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    ward_no = models.CharField(max_length=30)
    Tole = models.CharField(max_length=30)
    pharmacy = models.ForeignKey(PharmacistDetail, on_delete=models.CASCADE)


    def __str__(self):
        return self.city
