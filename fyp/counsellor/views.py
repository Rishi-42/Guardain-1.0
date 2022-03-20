from django.shortcuts import render
from .forms import BlogForm
from .models import BlogModel

def add_blog(request):
    context = {'form' : BlogForm}
    # try:
    #     if request.method == 'POST':
    #         form = BlogForm(request.POST)
    #         print(request.FILES)
    #         image = request.FILES['image']
    #         title = request.POST.get('title')
    #         user = request.user
            
    #         if form.is_valid():
    #             content = form.cleaned_data['content']
            
    #         blog_obj = BlogModel.objects.create(
    #             user = user , title = title, 
    #             content = content, image = image
    #         )
    #         print(blog_obj)
    #         return redirect('/add-blog/')
            
            
    
    # except Exception as e :
    #     print(e)
    
    return render(request , 'add_blog.html' , context)
