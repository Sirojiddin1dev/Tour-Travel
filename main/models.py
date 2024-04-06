from django.db import models


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