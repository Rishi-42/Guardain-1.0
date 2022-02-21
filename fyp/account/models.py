from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password, user_type):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            user_type = user_type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_customer(self, first_name, last_name, email, username, password):

        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        user.is_counsellor= True
        user.is_active=True
        user.save(using=self._db)
        return user

    def create_counsellor(self, first_name, last_name, email, username, password, license_no):
        if not license_no:
            raise ValueError('Counsellors must have a license number')

        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            license_no = license_no,
        )

        user.is_counsellor= True
        user.is_active=True
        user.save(using=self._db)
        return user

    def create_pharmacist(self, first_name, last_name, email, username, password, license_no, registration_no):
        if not license_no:
            raise ValueError('Pharmacists must have a license number')
        if not registration_no:
            raise ValueError('Pharmacists must have a registration number')

        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            license_no = license_no,
            registration_no = registration_no,
        )

        user.is_pharmacist= True
        user.is_active=True
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password, user_type):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
            user_type=user_type,
        )
        usert = None
        usert = Type_user(user=user,is_admin=True)
        usert.save()
        # user.is_customer=True
        user.is_superuser= True
        user.is_active=True
        user.is_staff=True
        user.is_admin=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    licence_no = models.CharField(max_length=30, unique=True, null=True, blank=True)
    user_type = models.CharField(max_length=30, null=True, blank=True)
    registration_no = models.CharField(max_length=30, unique=True, null=True, blank=True)

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
    
    def get_username(self):
        return self.username
        
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

class Type_user(models.Model):
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_pharmacist = models.BooleanField(default=False)
    is_counsellor = models.BooleanField(default=False)
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
        if self.is_customer == True:
            return Account.get_username(self.user) + " - is_customer"
        elif self.is_counsellor == True:
            return Account.get_username(self.user) + " - is_counsellor"
        elif self.is_pharmacist == True:
            return Account.get_username(self.user) + " - is_pharmacist"
        elif self.is_admin == True:
            return Account.get_username(self.user) + " - is_admin"




class PharmacistDetail(models.Model):
    pharmacy_name = models.CharField(max_length=100, blank=False, unique=True)
    phone_no = models.CharField(max_length=10, unique=True)
    registration_no = models.IntegerField(unique=True)
    pharmacy_email = models.EmailField(max_length=100, unique=True)
    registered_doc = models.FileField(upload_to='pharmacy/pharmacist_registred_document')
    profile_image = models.ImageField(upload_to='pharmacy/pharmacist_profile_image')
    work_start = models.CharField(max_length=2)
    work_end = models.CharField(max_length=2)
    description = models.CharField(max_length=500)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pharmacy_name
