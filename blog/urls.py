
from django.urls import path 
from . import views    # from current directory import views.py

urlpatterns = [
    path('' , views.home , name ='blog-home'),  # empty path means home page of our blog app
    path ('about/' , views.about , name = 'blog-about')

]
