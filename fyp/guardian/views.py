from multiprocessing import context
from urllib.error import ContentTooShortError
from django.shortcuts import render, get_object_or_404
from account.models import CounsellorDetail, PharmacistDetail, Adresses
from address.models import City
from rating.models import ReviewRating
from counsellor.models import BlogModel
from pharmacy.models import Add_product, Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from orders.models import Order, Payment
from booking.models import Meeting




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

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Add_product.objects.order_by('-created_date').filter(Q(product_name__icontains=keyword) | Q(contraindiction__icontains=keyword) | Q(indiction__icontains=keyword) | Q(adverse_effect__icontains=keyword) | Q(special_precautions__icontains=keyword))
            paginator = Paginator(products, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            product_count = products.count()
    
    content = {
        'products': page_obj,
        'product_count': product_count,
    }
          
    return render(request, 'medicine.html', content)


def dashboardcustomer(request):
    current_user = request.user
    orders = Order.objects.filter(user=current_user)
    context = {
        'orders' : orders,
    }

    return render(request, 'dashboardcustomer.html', context)

def customerbook(request):
    current_user = request.user
    meetings = Meeting.objects.filter(client_details=current_user)
    from datetime import date
    today = date.today()
    context = {
        'meetings' : meetings,
        'today' : today,
    }
    return render(request, 'customerbook.html', context)

def customerreviewed(request):
    current_user = request.user
    reviews = ReviewRating.objects.filter(user=current_user)
    context = {
        'reviews' : reviews,
    }
    return render(request, 'customerreviewed.html', context)

def paymentlog(request):
    current_user = request.user
    payments = Payment.objects.filter(user=current_user)
    context = {
        'payments' : payments,
    }
    return render(request, 'paymentlog.html', context)