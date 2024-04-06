from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_url'),
    path('blog/', blog_view, name='blog_url'),
    path('single-blog/<int:pk>/', single_blog_view, name='single_blog_url')
]
