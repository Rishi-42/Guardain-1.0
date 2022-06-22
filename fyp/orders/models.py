from django.db import models
from account.models import Account, PharmacistDetail
from pharmacy.models import Add_product
# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=150)
    payment_amount = models.CharField(max_length=150)
    status = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id


    
class Order(models.Model):
    status = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
        ('Failed', 'Failed'),
        ('New', 'New'),
    )

    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
    order_number = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    building = models.CharField(max_length=50, null=True)
    province = models.CharField(max_length=50)
    street = models.CharField(max_length=150)
    tax = models.CharField(max_length=50)
    order_total = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=status, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=50)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Add_product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    ordered = models.BooleanField(default=False)
    pharmacy = models.ForeignKey(PharmacistDetail, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name