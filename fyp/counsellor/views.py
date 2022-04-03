from django.shortcuts import render
from django.contrib import messages
from account.models import CounsellorDetail, Account
from .forms import BlogForm
from .models import BlogModel

# def add_blog(request):
#     context = {'form' : BlogForm}
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
    
    # return render(request , 'add_blog.html' , context)


def dashboardcounsellor(request):
    current_user = request.user
    user_email = current_user.email
    user_id=Account.objects.get(email=user_email)
    counsellor_name = CounsellorDetail.objects.get(user_id=user_id)

    form = BlogForm(request.POST, request.FILES)
    print(form.is_valid())
    if form.is_valid():
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        image = form.cleaned_data.get('image')
        slug = form.cleaned_data.get('slug')
        add_blog = BlogModel(title=title, content=content, image=image, slug=slug, counsellor_name_id=counsellor_name)
        add_blog.save()

        messages.success(request, 'Blog added successfully')
        return render(request, 'counsellor/dashboardcounsellor.html', {'form': form})
    else:
        form = BlogForm()
    context = {
        'form' : BlogForm
        }
    
    return render(request , 'counsellor/dashboardcounsellor.html' , context)
    

    
def added_blog(request):
    
    # getting the user id and their counsellor id
    current_user = request.user
    user_name = current_user.id
    user_counsellor = CounsellorDetail.objects.get(user_id=user_name)
    print(user_counsellor)
    counsellor_id = user_counsellor.id

    # getting the blog of the user
    blogs = BlogModel.objects.filter(counsellor_name_id=counsellor_id)
    context = {
        'blogs': blogs,
    }
    return render(request, 'counsellor/added_blogs.html', context)
