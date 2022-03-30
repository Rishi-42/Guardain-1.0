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
    pass