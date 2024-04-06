from .models import Blog, Comment, About, Banner, Gallery, Info, User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib import messages


def create_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        try:
            User.objects.create_user(
                username=username,
                password=password,
                phone_number=phone_number,
                email=email,
            )
            return redirect('index_url')
        except IntegrityError:
            error_message = "This username is already taken. Please choose a different one."
            messages.error(request, error_message)
            return render(request, 'account-pages--signup.html')

    return render(request, 'account-pages--signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('index_url')
    return render(request, 'account-pages--login.html')


def my_profile_view(request, pk):
    context = {
        'info': Info.objects.last(),
        'user': request.user
    }
    return render(request, 'my-account-pages--dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect('login_url')


def index_view(request):
    context = {
        'about': About.objects.all(),
        'banner': Banner.objects.all().order_by('-id')[:2],
        'info': Info.objects.last()
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
        return redirect("single_blog_url", pk)
    return render(request, 'single.html', context)


def gallery_view(request):
    context = {
        'gallery': Gallery.objects.all(),
    }
    return render(request, 'gallery-page.html', context)