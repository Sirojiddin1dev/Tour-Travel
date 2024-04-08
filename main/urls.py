from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_url'),
    path('blog/', blog_view, name='blog_url'),
    path('single-blog/<int:pk>/', single_blog_view, name='single_blog_url'),
    path('gallery', gallery_view, name='gallery_url'),
    path('register/', create_user_view, name='register_url'),
    path('login/', login_view, name='login_url'),
    path('my-profile/', my_profile_view, name='my_profile_url'),
    path('logout/', logout_view, name='logout_url'),
    path('set-contact-data/', set_contact_data, name='set_contact_data')
]
