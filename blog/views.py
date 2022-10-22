from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    mypost = Blogpost.objects.all()
    return render(request, 'blog/index.html',
                  {'mypost': mypost})


def blogpost(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    # print(post.post_id)
    prev = post.post_id - 1
    next = post.post_id + 1
    # print(prev)
    return render(request, 'blog/blogpost.html', {'post': post, 'prev': prev, 'next': next})

