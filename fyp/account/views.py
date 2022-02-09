
from django.shortcuts import render, redirect
from .forms import RegistrationForm, RegistrationFormPharmacy
from .models import Account, Type_user, PharmacistDetail
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
                send_email = EmailMessage(mail_subject, message, to=[to_email])
                send_email.send()
                messages.success(request, 'Account created successfully. Please verify your email and login to continue.')
                return render(request, 'account/login.html')
            elif user_type == 'counsellor':
                usert = Type_user(user=user,is_counsellor=True)
                usert.save()
                context = {
                    'email': email,
                }                   
                return render(request, 'account/counsellor_register.html')
            elif user_type == 'pharmacist':
                usert = Type_user(user=user,is_pharmacist=True)
                usert.save()
                return render(request, 'account/pharmacyregister.html')
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
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'account/login.html')

    return render(request, 'account/login.html')

def pharmacyregister(request):
    # form = RegistrationFormPharmacy()
    # if request.method == 'POST':
    #     # get data from account model
    #     form = RegistrationFormPharmacy(request.POST)
    #     if form.is_valid():
            
    #         pharmacy = PharmacistDetail()
    #         pharmacy.save()
            
    #         # USER activation
    #         # current_site = get_current_site(request)
    #         # mail_subject = "Please activate your Guardian account"
    #         # message = render_to_string('account/account_verification_email.html',{
    #         #     'user' : pharmacy,
    #         #     'domain' : current_site,
    #         #     'uid' : urlsafe_base64_encode(force_bytes(pharmacy.pk)),
    #         #     'token' : default_token_generator.make_token(pharmacy),
    #         # })
    #         # to_email = email
    #         # send_email = EmailMessage(mail_subject, message, to=[to_email])
    #         # send_email.send()
    #         # messages.success(request, 'Account created successfully. Please verify your email and login to continue.')
    #         # return render(request, 'account/login.html')
            
    # else:
    #     form = RegistrationFormPharmacy()

    # context = {
    #     'form': form,
    # }
    return render(request, 'account/pharmacyregister.html')




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
