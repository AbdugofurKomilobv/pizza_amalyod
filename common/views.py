from django.shortcuts import render
from blogs.form import ContactPageForm,AboutPageForm

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

# ========

def contacts_page_view(request):
    if request.method == "GET":
      return render(request,template_name='pages/contact.html')
    
    elif request.method == "POST":
      form = ContactPageForm(request.POST)
      if form.is_valid():
          form.save()
      
      else:
          pass

      return render(request,template_name='pages/contact.html')





def about_page_view(request):
    return render(request,template_name="pages/about.html")
