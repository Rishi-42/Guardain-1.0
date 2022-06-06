from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadPrescriptionForm
from .models import UploadPrescription

def uploadprescription(request):
    form = UploadPrescriptionForm()
    if request.method == 'POST':
        form = UploadPrescriptionForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            prescription = form.cleaned_data['prescription']
            prescripted_by = form.cleaned_data['prescripted_by']
            prescripted_for = form.cleaned_data['prescripted_for']

            p_data = UploadPrescription(name=name, age=age, prescription=prescription, prescripted_by=prescripted_by, prescripted_for=prescripted_for)
            p_data.save()
            messages.success(
                request, "Thank you!")
            
            return render(request, 'prescription/uploadprescription.html', {'form': form})
    else:
        form = UploadPrescriptionForm()
    context = {
        'form': form,
    }
    return render(request, 'prescription/uploadprescription.html', context)

