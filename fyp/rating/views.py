from django.shortcuts import redirect
from account.models import PharmacistDetail
from .models import ReviewRating
from .forms import ReviewForm
from django.contrib import messages

# Create your views here.
def submit_review(request, pharmacy_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(pharmacy__id=pharmacy_id, user__id=request.user.id)
            print(reviews)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.pharmacy = PharmacistDetail.objects.get(id=pharmacy_id)
                data.user = request.user
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)