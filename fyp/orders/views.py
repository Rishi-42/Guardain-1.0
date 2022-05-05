from django.shortcuts import render, redirect
from cart.models import *
from .forms import OrderForm
from .models import *
import datetime
from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import JsonResponse
from pharmacy.models import Add_product


# for email
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

# Create your views here.
def _cart_i(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart



def payments(request):
    body = json.loads(request.body)
    print(body)
    order = Order.objects.get(user=request.user, is_ordered=False, order_number=body['orderID'])

    # Store transaction details inside Payment model
    payment = Payment(
        user = request.user,
        payment_id = body['transID'],
        payment_method = body['payment_method'],
        payment_amount = order.order_total,
        status = body['status'],
    )
    print(payment)
    payment.save()

    order.payment = payment
    order.is_ordered = True
    order.save()

    # Move the cart items to Order Product table
    cart = Cart.objects.get(cart_id=_cart_i(request))
    cart_items = CartItem.objects.filter(cart=cart, active=True)
    # cart_items = CartItem.objects.filter(user=request.user)

    for item in cart_items:
        orderproduct = OrderProduct()
        orderproduct.order_id = order.id
        orderproduct.payment = payment
        orderproduct.user_id = request.user.id
        orderproduct.product_id = item.product_id
        orderproduct.quantity = item.quantity
        orderproduct.price = item.product.cost
        orderproduct.ordered = True
        orderproduct.save()



        # Reduce the quantity of the sold products
        # product = Add_product.objects.get(id=item.product_id)
        # product.stock -= item.quantity
        # product.save()

    # Clear cart
    try:
        cart = Cart.objects.get(cart_id=_cart_i(request))
        CartItem.objects.filter(cart=cart).delete()
        # cart_items = CartItem.objects.filter(cart=cart, active=True)
    except ObjectDoesNotExist:
        pass  
    

    # # Send order recieved email to customer
    mail_subject = 'Thank you for your order!'
    message = render_to_string('order_recieved_email.html', {
        'user': request.user,
        'order': order,
    })
    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()

    # Send order number and transaction id back to sendData method via JsonResponse
    data = {
        'order_number': order.order_number,
        'transID': payment.payment_id,
    }
    return JsonResponse(data)





def place_order(request, total=0, quantity=0, cart_items=None):
    current_user = request.user
    try:
        cart = Cart.objects.get(cart_id=_cart_i(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.cost * cart_item.quantity)
            quantity += cart_item.quantity
        shipping_cost = (2 * total)/100
        grand_total = total + shipping_cost

    except ObjectDoesNotExist:
        pass
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data= Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address = form.cleaned_data['address']
            data.province = form.cleaned_data['province']
            data.street = form.cleaned_data['street']
            data.city = form.cleaned_data['city']
            data.building = form.cleaned_data['building']
            data.tax = shipping_cost
            data.order_total = grand_total
            data.status = 'New'
            data.ip = request.META['REMOTE_ADDR']
            data.save()
            
            
            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d") #20210305
            order_number = current_date + str(data.id)
            data.order_number = order_number
            print(order_number)
            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': shipping_cost,
                'grand_total': grand_total,
            }
            return render(request, 'payments.html', context)

    else:
        return redirect('checkout')

    

def order_complete(request):
    order_number = request.GET.get('order_number')
    transID = request.GET.get('payment_id')

    try:
        order = Order.objects.get(order_number=order_number, is_ordered=True)
        ordered_products = OrderProduct.objects.filter(order_id=order.id)

        subtotal = 0
        for i in ordered_products:
            subtotal += i.price * i.quantity

        payment = Payment.objects.get(payment_id=transID)

        context = {
            'order': order,
            'ordered_products': ordered_products,
            'order_number': order.order_number,
            'transID': payment.payment_id,
            'payment': payment,
            'subtotal': subtotal,
        }
        return render(request, 'order_complete.html', context)
    except (Payment.DoesNotExist, Order.DoesNotExist):
        return redirect('home')