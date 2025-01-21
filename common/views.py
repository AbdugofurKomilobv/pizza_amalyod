from django.shortcuts import render

def home_page_view(request):
    return render(request,template_name='index.html')



def about_page_view(request):
    return render(request,template_name="pages/about.html")

def resipies_page_view(request):
    return render(request,template_name="recipies/recipe-with-sidebar.html")

def contacts_page_view(request):
    return render(request,template_name='pages/contact.html')


def shop_page_view(request):
    return render(request,template_name='shop/shop.html')

def category_page_view(request):
    return render(request,template_name='recipies/category.html')

def blog_page_view(request):
    return render(request,template_name='blogs/blogs_list.html')