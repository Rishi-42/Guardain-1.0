# from django.db import models
# from pharmacy.models import Add_product
# from account.models import Account

# class ReviewRating(models.Model):
#     product = models.ForeignKey(Add_product, on_delete=models.CASCADE)
#     user = models.ForeignKey(Account, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=100, blank=True)
#     review = models.TextField(max_length=500, blank=True)
#     rating = models.FloatField()
#     ip = models.CharField(max_length=20, blank=True)
#     status = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.subject


# class ProductGallery(models.Model):
#     product = models.ForeignKey(Add_product, default=None, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='store/products', max_length=255)

#     def __str__(self):
#         return self.product.product_name

#     class Meta:
#         verbose_name = 'productgallery'
#         verbose_name_plural = 'product gallery'