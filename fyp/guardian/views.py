
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from account.models import Account, CounsellorDetail, PharmacistDetail
from address.models import City, Adresses
# from pharmacy.models import 


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
    return render(request, 'counsellor/dashboardcounsellor.html')

def dashboardpharmacist(request):
    return render(request, 'dashboardpharmacy.html')



def cities(request):
    cities_all = City.objects.all()
    context = {
        'cities_all' : cities_all,
    }
    return render(request, 'pharmacy_cities.html', context)


def pharmacies(request, city_slug=None):
    cities = None
    pharmacy =None
    
    if city_slug != None:
        cities = get_object_or_404(City, slug=city_slug)
        # address = City.objects.filter(slug=city_slug).values('name')
        
        # print(address)
        # add = Adresses.objects.get(city=address)
        # print(add)

        # users_on_that_city = Adresses.objects.filter(city=address)
        # pharmacy = users_on_that_city.filter(user_name__user_type='Pharmacy')

        # pharmacy = PharmacistDetail.objects.filter(adresses=address)
        # should refer to address of pharmacy from address models
        # pharmacy = PharmacistDetail.objects.filter(City=city_slug)
    
    else:
        pharmacy = PharmacistDetail.objects.all()
    context = {
        'pharmacies' :pharmacy
    }
   
    return render(request, 'pharmacy_city1.html', context)


def counsellors(request):
    counsellors_all = CounsellorDetail.objects.all()
    context = {
        'counsellors_all' : counsellors_all,
    }

    return render(request, 'counsellor.html', context)

def searchmed(request):
    return render(request, 'medicine.html')

def viewblogs(request):
    return render(request, 'viewblogs.html')