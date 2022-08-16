from django.db import models
from page.models import STATUS
from django.contrib.auth.models import User
DEFAULT_STATUS = "draft"

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200, 
        default="",
    )
    status = models.CharField(
        default=DEFAULT_STATUS, 
        choices=STATUS,
        max_length=10,
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class Blog_post(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=40)
    slug = models.SlugField(
        max_length=200, 
        default="",
    )
    content = models.TextField() 
    image = models.ImageField(upload_to="img")
    next_img = models.ImageField(upload_to="next")
    status = models.CharField(
        default="draft", 
        choices=STATUS,
        max_length=10,
    )
    author=models.CharField(max_length=100)
    
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    blog_name = models.ForeignKey(
        Blog_post,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE
    )
    content = models.TextField()
    status = models.CharField(
        default="published", 
        choices=STATUS,
        max_length=10,
    )
    createt_at = models.DateTimeField(auto_now_add=True)