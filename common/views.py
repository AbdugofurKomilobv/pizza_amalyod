from django.shortcuts import render

def home_page_view(request):
    return render(request,template_name='index.html')



def about_page_view(request):
    return render(request,template_name="pages/about.html")
