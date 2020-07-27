from django.shortcuts import render
from .models import Post 


''' This function  is going to handle the traffic from the home page 
of our blog . It takes a request argument '''
posts = Post.objects.all() 



def home (request ) :
    context = {
        'posts' : posts
    }
    return render(request , 'blog/home.html' , context  )

def  about (request ) :
    return render(request , 'blog/about.html' , {"title" : "About"})

