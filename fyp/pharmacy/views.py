from django.shortcuts import render, redirect
from account.models import PharmacistDetail, Account
from pharmacy.forms import AddProductForm
from pharmacy.models import Add_product
from django.contrib import messages



# Create your views here.
def dashboardpharmacist(request):


    current_user = request.user
    user_email = current_user.email
    user_id=Account.objects.get(email=user_email)
    pharmacy_name = PharmacistDetail.objects.get(user_id=user_id)

    form = AddProductForm(request.POST, request.FILES)
    print(form.is_valid())
    if form.is_valid():
        product_name = form.cleaned_data.get('product_name')
        slug = form.cleaned_data.get('slug')
        image = form.cleaned_data.get('image')
        cost = form.cleaned_data.get('cost')
        stock = form.cleaned_data.get('stock')
        dose_child = form.cleaned_data.get('dose_child')
        dose_adult = form.cleaned_data.get('dose_adult')
        category = form.cleaned_data.get('category')
        contraindiction = form.cleaned_data.get('contraindiction')
        indiction = form.cleaned_data.get('indiction')
        special_precautions = form.cleaned_data.get('special_precautions')
        adverse_effect = form.cleaned_data.get('adverse_effect')

        add_product = Add_product(product_name=product_name, slug=slug, image=image, cost=cost, stock=stock, dose_child=dose_child, dose_adult=dose_adult, category=category, contraindiction=contraindiction, indiction=indiction, special_precautions=special_precautions, adverse_effect=adverse_effect, pharmacy_name_id=pharmacy_name)
        add_product.save()

        messages.success(request, 'Product added successfully')
        return render(request, 'pharmacy/dashboardpharmacy.html', {'form': form})
    else:
        form = AddProductForm()
    context = {
        'form': form,
    }
    return render(request, 'pharmacy/dashboardpharmacy.html', context)


def added_product(request):

    # getting the user id and their pharmacy id
    current_user = request.user
    user_name = current_user.id
    user_pharmacy = PharmacistDetail.objects.get(user_id=user_name)
    print(user_pharmacy)
    pharmacy_id = user_pharmacy.id

    # getting the products of the user
    products = Add_product.objects.filter(pharmacy_name_id=pharmacy_id)
    context = {
        'products': products,
    }
    return render(request, 'pharmacy/added_product.html', context)
    
def edit(request, id):
    todos = Add_product.objects.get(id=id)
    context = {'todo': todos}
    return render(request, 'pharmacy/edit.html', context)

    
def delete(request, id):
    todo = Add_product.objects.get(id=id)
    todo.delete()
    return render(request, 'pharmacy/added_product.html')

def update(request, id):
    todo = Add_product.objects.get(id=id)
    form = AddProductForm(request.POST, request.FILES)

    print(form.is_valid())
    if form.is_valid():
        form.save()
        return redirect('/pharmacy/added_product')
    context = {
        'form': form,
    }
    return render(request, 'pharmacy/edit.html', context)
