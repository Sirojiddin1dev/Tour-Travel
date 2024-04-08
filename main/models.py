from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, verbose_name='Telefon raqam', null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ),
    ])

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=55)
    title_img = models.ImageField(upload_to='title_image/')
    description = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    single_img = models.ImageField(upload_to='single_img/')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    date = models.DateTimeField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return self.blog.title


class About(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=155)
    image = models.ImageField(upload_to='about_img/')
    text = models.TextField()

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    image = models.ImageField(upload_to='banner_img/')


class Gallery(models.Model):
    title = models.CharField(max_length=55)
    image = models.ImageField(upload_to='banner_img/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'


class Info(models.Model):
    icon = models.ImageField(upload_to='icon_img/')
    linkedin = models.CharField(max_length=55)
    facebook = models.CharField(max_length=55)
    instagram = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=55)
    email = models.EmailField()
    address = models.CharField(max_length=155)


class Contact(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    phone = models.CharField(max_length=55)
    message = models.TextField()
    email = models.EmailField( max_length=254)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
