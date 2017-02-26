from django.shortcuts import render, get_object_or_404
from .models import BlogPost


# Create your views here.
def post_list(request):
    posts = BlogPost.published.all()
    return render(request,
                  'blog/list.html',
                  {'posts': posts})


def post_detail(request, year, month, day, post):
    posts = get_object_or_404(BlogPost, slug=post,
                              status='published',
                              publish__year=year,
                              publish__month=month,
                              publish__day=day)
    return render(request,
                  'blog/detail.html',
                  {'posts': posts})
