
from django.shortcuts import render, redirect
from .forms import RegistrationForm, RegistrationFormPharmacy, Address_form, RegistrationFormCounsellor
from .models import Account, Type_user, PharmacistDetail, CounsellorDetail
from address.models import Adresses, District, City
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# for verification email
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user_type = form.cleaned_data['user_type']
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password, user_type=user_type)
            user.save()
            
            # USER activation
            current_site = get_current_site(request)
            mail_subject = "Please activate your Guardian account"
            message = render_to_string('account/account_verification_email.html',{
                'user' : user,
                'domain' : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user),
            })
            to_email = email
            usert = None
            if user_type == 'customer':
                usert = Type_user(user=user,is_customer=True)
                usert.save()
            elif user_type == 'counsellor':
                usert = Type_user(user=user,is_counsellor=True)
                usert.save()                    
            elif user_type == 'pharmacist':
                usert = Type_user(user=user,is_pharmacist=True)
                usert.save()                 
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            # messages.success(request, 'Account created successfully. Please verify your email and login to continue.')
            return redirect('/account/login/?command=verification&email='+email)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'account/customer_register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            type = user.user_type
            if type == "customer":
                return redirect('home')
            elif type == "pharmacist":
                current_user = request.user
                if  PharmacistDetail.objects.filter(user_id=current_user).exists():
                    return redirect('dashboardpharmacist')
                else:
                    return redirect('pharmacyregister')
            elif type == "counsellor":
                current_user = request.user
                if  CounsellorDetail.objects.filter(user_id=current_user).exists():
                    return redirect('dashboardcounsellor')
                else:
                    return redirect('counsellorregister')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'account/login.html')

    return render(request, 'account/login.html')

def pharmacyregister(request):
    current_user = request.user
    user_email = current_user.email
    user_name = current_user.id
    form = RegistrationFormPharmacy()
    form_add = Address_form()
    if request.method == 'POST':
        # get data from account mode
        form = RegistrationFormPharmacy(request.POST, request.FILES)
        form_add = Address_form(request.POST)
        if form.is_valid() and form_add.is_valid():
            pharmacy_name = form.cleaned_data['pharmacy_name']
            # profile_image=request.FILES['profile_image']
            profile_image = form.cleaned_data['profile_image']
            pharmacy_email = form.cleaned_data['pharmacy_email']
            phone_no = form.cleaned_data['phone_no']
            registration_no = form.cleaned_data['registration_no']
            registered_doc = form.cleaned_data['registered_doc']
            work_start = form.cleaned_data['work_start']
            work_end = form.cleaned_data['work_end']
            description = form.cleaned_data['description']


            province = form_add.cleaned_data['province']
            district = form_add.cleaned_data['district']
            city = form_add.cleaned_data['city']
            ward_no = form_add.cleaned_data['ward_no']
            tole = form_add.cleaned_data['tole']

            pharmacy = PharmacistDetail(pharmacy_name=pharmacy_name, profile_image=profile_image, pharmacy_email=pharmacy_email, phone_no=phone_no, registration_no=registration_no, registered_doc=registered_doc, work_start=work_start, work_end=work_end, description=description, user_id=Account.objects.get(email = user_email))
            address = Adresses(province=province, district=district, city=city, ward_no=ward_no, tole=tole, user_name=Account.objects.get(id = user_name))
            pharmacy.save()
            address.save()
            return render(request, 'account/login.html')
              
    else:
        form = RegistrationFormPharmacy()
        form_add = Address_form()

    context = {
        'form': form,
        'form_add': form_add,
    }
    return render(request, 'account/pharmacyregister.html', context)



def load_districts(request):
    province_id = request.GET.get('province')
    districts = District.objects.filter(province_id=province_id).order_by('name')
    return render(request, 'account/district_dropdown_list_options.html', {'districts': districts})

def load_cities(request):
    district_id = request.GET.get('district')
    cities = City.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'account/city_dropdown_list_options.html', {'cities': cities})












def counsellorregister(request):
    current_user = request.user
    user_email = current_user.email
    user_name = current_user.id
    form = RegistrationFormCounsellor()
    form_add = Address_form()
    if request.method == 'POST':
        # get data from account mode
        form = RegistrationFormCounsellor(request.POST, request.FILES)
        form_add = Address_form(request.POST)
        print(form.is_valid())
        print(form_add.is_valid())
        if form.is_valid() and form_add.is_valid():
            counsellor_name = form.cleaned_data['counsellor_name']
            # profile_image=request.FILES['profile_image']
            profile_image = form.cleaned_data['profile_image']
            counsellor_email = form.cleaned_data['counsellor_email']
            phone_no = form.cleaned_data['phone_no']
            registration_no = form.cleaned_data['registration_no']
            registered_doc = form.cleaned_data['registered_doc']
            work_start = form.cleaned_data['work_start']
            work_end = form.cleaned_data['work_end']
            description = form.cleaned_data['description']


            province = form_add.cleaned_data['province']
            district = form_add.cleaned_data['district']
            city = form_add.cleaned_data['city']
            ward_no = form_add.cleaned_data['ward_no']
            tole = form_add.cleaned_data['tole']

            counsellor = CounsellorDetail(counsellor_name=counsellor_name, profile_image=profile_image, counsellor_email=counsellor_email, phone_no=phone_no, registration_no=registration_no, registered_doc=registered_doc, work_start=work_start, work_end=work_end, description=description, user_id=Account.objects.get(email = user_email))
            address = Adresses(province=province, district=district, city=city, ward_no=ward_no, tole=tole, user_name=Account.objects.get(id = user_name))
            counsellor.save()
            address.save()
            return render(request, 'account/login.html')
              
    else:
        form = RegistrationFormCounsellor()
        form_add = Address_form()

    context = {
        'form': form,
        'form_add': form_add,
    }
    return render(request, 'account/counsellorregister.html', context)



@login_required(login_url= 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out!")
    return render(request, 'account/login.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Congratulations! Your account is activated.")
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')

def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            # reset password
            current_site = get_current_site(request)
            mail_subject = "Reset Password"
            message = render_to_string('account/reset_password_email.html',{
                'user' : user,
                'domain' : current_site,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Password reset email has been send to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid email')
            return render(request, 'account/forgotpassword.html')
    
    return render(request, 'account/forgotpassword.html')


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect	('resetpassword')
    else:
        messages.error(request, 'Invalid reset password link')
        return redirect('forgotpassword')
    
def resetpassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST.get('confirm_password', False);
        if password == confirm_password:
            uid = request.session['uid']
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successfully')
            return redirect('login')
        else:
            messages.error(request, 'Password not matched')
            return redirect('resetpassword')
    return render(request, 'account/resetpassword.html')