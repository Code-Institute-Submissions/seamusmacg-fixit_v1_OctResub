from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost
from django.contrib import messages

# Create your views here.

# def blog(request):
#     return render(request, 'blog/blog.html')

class MainBlog(ListView):
    model = BlogPost
    template_name = 'blog/blog.html'


class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'


class AddBlog(CreateView):
    model = BlogPost
    template_name = 'blog/write_blog.html'
    fields = '__all__'

