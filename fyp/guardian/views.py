from django.shortcuts import render
from account.models import Account 


def home(request):
    # user_details = Account.objects.
    # current_user = request.user
    # print(current_user)
    # user_details = Account.objects.get(email=current_user)
    # print(user_details.user_type)
    # return render(request, 'home.html', {'user_details': user_details})
    return render(request, 'home.html')

def placeorder(request):
    return render(request, 'place-order.html')

def counsellor(request):
    return render(request, 'counsellor.html')

def cart(request):
    return render(request, 'cart.html')

def productdetail(request):
    return render(request, 'product-detail.html')

def test(request):
    return render(request, 'test.html')

def dashboardcounsellor(request):
    return render(request, 'dashboardcounsellor.html')

def dashboardpharmacist(request):
    return render(request, 'dashboardpharmacy.html')