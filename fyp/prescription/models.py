from django.db import models

class UploadPrescription(models.Model):
    name = models.CharField(max_length=35)
    age = models.PositiveIntegerField()
    prescription = models.FileField(upload_to='prescription_img/')
    prescripted_by = models.CharField(max_length=35)
    prescripted_for = models.CharField(max_length=50)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name