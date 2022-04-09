from .models import Category

def category_link(request):
    links = Category.objects.all()
    return dict(links=links)