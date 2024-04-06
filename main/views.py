from django.shortcuts import render, redirect
from .models import Blog, Comment, About, Banner


def index_view(request):
    context = {
        'about': About.objects.all(),
        'banner': Banner.objects.all().order_by('-id')[:2],
    }
    return render(request, 'index.html', context)


def blog_view(request):
    context = {
        'blog': Blog.objects.all()
    }
    return render(request, 'blog-listings--no-sidebar.html', context)


def single_blog_view(request, pk):
    single_blog = Blog.objects.get(pk=pk)
    context = {
        'single_blog': single_blog
    }
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        Comment.objects.create(
            name=name,
            message=message,
            blog=single_blog,
        )
        return redirect("single_blog_url", pk=single_blog.id)
    return render(request, 'blog-listings--no-sidebar.html', context)

