from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from address.models import Province, District, City
from .gen_slug import *
from django.urls import reverse

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password, user_type):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password, user_type):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type,
        )
        usert = None
        usert = Type_user(user=user, is_administrator=True)
        usert.save()
        # user.is_customer=True
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    user_type = models.CharField(max_length=30, null=True, blank=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'user_type']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Type_user(models.Model):
    is_administrator = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_pharmacist = models.BooleanField(default=False)
    is_counsellor = models.BooleanField(default=False)
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class PharmacistDetail(models.Model):
    pharmacy_name = models.CharField(max_length=100, blank=False, unique=True)
    slug = models.SlugField(max_length=200, null = True, blank = True)
    profile_image = models.ImageField(
        upload_to='profile/pharmacist_profile_image')
    pharmacy_email = models.EmailField(max_length=100, unique=True)
    phone_no = models.CharField(max_length=10, unique=True)
    registration_no = models.CharField(max_length=15, unique=True)
    registered_doc = models.FileField(
        upload_to='doc/pharmacist_registred_document')
    work_start = models.CharField(max_length=2)
    work_end = models.CharField(max_length=2)
    description = models.CharField(max_length=500)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pharmacy_name
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.pharmacy_name)
        super(PharmacistDetail, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("ind_pharmacy", args=[self.city.slug,self.slug])

class CounsellorDetail(models.Model):
    counsellor_name = models.CharField(
        max_length=100, blank=False, unique=True)
    profile_image = models.ImageField(
        upload_to='profile/counsellor_profile_image')
    counsellor_email = models.EmailField(max_length=100, unique=True)
    phone_no = models.CharField(max_length=10, unique=True)
    registration_no = models.CharField(max_length=15, unique=True)
    registered_doc = models.FileField(
        upload_to='doc/counsellor_registred_document')
    work_start = models.CharField(max_length=2)
    work_end = models.CharField(max_length=2)
    description = models.CharField(max_length=500)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.counsellor_name

    def get_url(self):
        return reverse("counselor_detail", args=[self.id])

class Adresses(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    ward_no = models.CharField(max_length=30)
    tole = models.CharField(max_length=30)
    user_name = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)



    def __str__(self):
        return self.tole
        