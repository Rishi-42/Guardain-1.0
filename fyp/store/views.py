from importlib.resources import contents
from django.shortcuts import render, get_object_or_404
from pharmacy.models import Add_product, Category
from cart.views import _cart_id
from cart.models import CartItem
# Create your views here.


def all_product(request, pharmacy_id, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Add_product.objects.filter(pharmacy_name_id=pharmacy_id, category=categories)
        product_count = products.count()
        pharmacy_id = pharmacy_id
    else:
        products = Add_product.objects.filter(pharmacy_name_id=pharmacy_id)
        product_count = products.count()
    content = {
        'products': products,
        'product_count': product_count,
        'pharmacy_id': pharmacy_id,
    }

    return render(request, 'store.html', content)

def product_detail(request, pharmacy_id, category_slug, product_slug):
    try:
        single_product = Add_product.objects.get(pharmacy_name_id=pharmacy_id, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
       

    
    except Exception as e:
        raise e
    content = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'product_detail.html', content)



def store(request):
    return render(request, 'store.html')