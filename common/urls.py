from django.urls import path
from common.views import *

app_name = 'pages'

urlpatterns = [
    path('about/',about_page_view,name='about'),
    path('recipies/', resipies_page_view, name="recipies"),
    path('contact/',contacts_page_view,name='contact'),
    path('shop/',shop_page_view,name='shop'),
    path('category/',category_page_view,name='category'),
    path('blog/',blog_page_view,name='blog'),
    path('',home_page_view,name='home'),
]