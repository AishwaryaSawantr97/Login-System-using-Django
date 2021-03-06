from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Aishwarya Sawant',
        'title': 'Blog post',
        'content': 'Content',
        'date_posted':'September 20, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
