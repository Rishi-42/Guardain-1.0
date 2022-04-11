from django.shortcuts import render
from counsellor.models import BlogModel




def blogs(request):
    blogs = BlogModel.objects.all()
    context = {
        'blog_obj' : blogs,
    }
    return render(request, 'blog/blogs.html', context)

def blog_detail(request, slug):
    blog = BlogModel.objects.get(slug=slug)
    context = {
        'blog_obj' : blog,
    }
    return render(request, 'blog/blog_detail.html', context)