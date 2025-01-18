from django.urls import path
from common.views import home_page_view


urlpatterns = [
    path('',home_page_view)
]