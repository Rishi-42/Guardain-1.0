from importlib.resources import contents
from django.shortcuts import render, get_object_or_404
from account.models import PharmacistDetail
from pharmacy.models import Add_product, Category
from cart.views import _cart_id
from cart.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
from django.http import HttpResponse
from django.db.models import Q

def all_product(request, pharmacy_id, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Add_product.objects.filter(pharmacy_name_id=pharmacy_id, category=categories)
        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        product_count = products.count()
        pharmacy_id = pharmacy_id
        pharmacyname = PharmacistDetail.objects.get(id=pharmacy_id)
        print(pharmacyname)
    else:
        products = Add_product.objects.filter(pharmacy_name_id=pharmacy_id)
        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        pharmacyname = PharmacistDetail.objects.get(id=pharmacy_id)
        print(pharmacyname)
        
        product_count = products.count()
    content = {
        'products': page_obj,
        'product_count': product_count,
        'pharmacy_id': pharmacy_id,
        'pharmacyname': pharmacyname,
    }

    return render(request, 'store.html', content)

def product_detail(request, pharmacy_id, category_slug, product_slug):
    try:
        single_product = Add_product.objects.get(pharmacy_name_id=pharmacy_id, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        contraindictions = single_product.contraindiction.split(',')
        indications = single_product.indiction.split(',')
        adverse_effects = single_product.adverse_effect.split(',')
        special_precautions = single_product.special_precautions.split(',')


    
    except Exception as e:
        raise e
    content = {
        'single_product': single_product,
        'in_cart': in_cart,
        'contraindictions': contraindictions,
        'indications': indications,
        'adverse_effects': adverse_effects,
        'special_precautions': special_precautions,
    }
    return render(request, 'product_detail.html', content)





