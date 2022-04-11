from django.shortcuts import render
from account.models import CounsellorDetail
# Create your views here.

def counselor(request):
    counsellors_all = CounsellorDetail.objects.all()
    context = {
        'counsellors_all' : counsellors_all,
    }

    return render(request, 'counsellor.html', context)


def counselor_detail(request, pk):
    counsellor = CounsellorDetail.objects.get(pk=pk)
    context = {
        'counsellor' : counsellor,
    }

    return render(request, 'counsellor_individual.html', context)