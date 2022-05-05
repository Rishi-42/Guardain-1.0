from multiprocessing import context
from urllib.error import ContentTooShortError
from django.shortcuts import render, get_object_or_404
from account.models import CounsellorDetail, PharmacistDetail, Adresses
from address.models import City
from rating.models import ReviewRating
from counsellor.models import BlogModel
from pharmacy.models import Add_product, Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator




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



def productdetail(request):
    return render(request, 'product-detail.html')

def test(request):
    return render(request, 'test.html')


def cities(request):
    cities_all = City.objects.all().order_by('id')
    paginator = Paginator(cities_all, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'cities_all' : page_obj,

    }
    return render(request, 'pharmacy_cities.html', context)






def pharmacies(request, city_slug=None):
    cities = None
    pharmacy =None
    
    if city_slug != None:
        cities = get_object_or_404(City, slug=city_slug)
        pharmacy = PharmacistDetail.objects.filter(city=cities).order_by('id')
        paginator = Paginator(pharmacy, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
    else:
        pharmacy = PharmacistDetail.objects.all().order_by('id')
        paginator = Paginator(pharmacy, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    context = {
        'pharmacies' :page_obj
    }
   
    return render(request, 'pharmacy_city1.html', context)

def ind_pharmacy(request, city_slug, pharmacy_slug):
    try:
        individual_pharmacy = PharmacistDetail.objects.get(city__slug=city_slug, slug=pharmacy_slug)
        reviews = ReviewRating.objects.filter(pharmacy_id=individual_pharmacy.id, status=True)
    
    except Exception as e:
        raise e
    
    # Get the reviews
    

    context ={
        'individual_pharmacy' : individual_pharmacy,
        'reviews' : reviews
    }
    return render(request, 'individual_pharmacy.html', context)


def searchmed(request):
    return render(request, 'medicine.html')


def readblog(request):
    blogs = BlogModel.objects.filter(id=1)
    print(blogs)
    context = {
        'blog_obj' : blogs,
    }
    return render(request, 'readblog.html', context)




