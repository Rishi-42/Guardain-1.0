
from multiprocessing import context
from urllib.error import ContentTooShortError
from django.shortcuts import render, get_object_or_404
from account.models import CounsellorDetail, PharmacistDetail, Adresses
from address.models import City
from counsellor.models import BlogModel
from pharmacy.models import Add_product, Category
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

        pharmacy = PharmacistDetail.objects.filter(city=cities)
    
    else:
        pharmacy = PharmacistDetail.objects.all()
    context = {
        'pharmacies' :pharmacy
    }
   
    return render(request, 'pharmacy_city1.html', context)

def ind_pharmacy(request, city_slug, pharmacy_slug):
    try:
        individual_pharmacy = PharmacistDetail.objects.get(city__slug=city_slug, slug=pharmacy_slug)
    except Exception as e:
        raise e

    context ={
        'individual_pharmacy' : individual_pharmacy
    }
    return render(request, 'individual_pharmacy.html', context)

def counsellors(request):
    counsellors_all = CounsellorDetail.objects.all()
    context = {
        'counsellors_all' : counsellors_all,
    }

    return render(request, 'counsellor.html', context)

def searchmed(request):
    return render(request, 'medicine.html')

def viewblogs(request):
    blogs = BlogModel.objects.all()
    print(blogs)
    context = {
        'blog_obj' : blogs,
    }
    return render(request, 'blogs.html', context)

def readblog(request):
    blogs = BlogModel.objects.filter(id=1)
    print(blogs)
    context = {
        'blog_obj' : blogs,
    }
    return render(request, 'readblog.html', context)

def individual_pharmacy(request):
    pharmacy = PharmacistDetail.objects.filter(pharmacy_name='Test Pharmacy nepal')
    print(pharmacy)
    context = {
        'pharmacy' : pharmacy,
    }
    return render(request, 'individual_pharmacy.html', context)

def store(request):
    medicine = Add_product.objects.filter(pharmacy_name_id='2')
    categories = Category.objects.all()

    context ={
        'medicine' :medicine ,
        'categories' : categories
    }
    return render(request, 'store.html', context)