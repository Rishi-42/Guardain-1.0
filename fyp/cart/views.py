from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from pharmacy.models import Add_product
from django.contrib.auth.decorators import login_required

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
@login_required(login_url='login')
def add_cart(request, product_id):
    product = Add_product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product =get_object_or_404(Add_product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product =get_object_or_404(Add_product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.cost * cart_item.quantity)
            quantity += cart_item.quantity
        shipping_cost = (2 * total)/100
        grand_total = total + shipping_cost

    except ObjectDoesNotExist:
        pass

    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items,
        'shipping_cost' : shipping_cost,
        'grand_total' : grand_total,
    }
    return render(request, 'cart.html', context)