from django.db import models

STATUS = [
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200, 
        default="",
    )
    cover_image = models.ImageField() 
    content = models.TextField()
    status = models.CharField(
        default="draft", 
        choices=STATUS,
        max_length=10,
    )
    sidebar = models.BooleanField(default = True)
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    user_name = models.CharField(max_length=200)
    mail = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
class Info(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(
        default="draft", 
        choices=STATUS,
        max_length=10,
    )
    cover_image = models.ImageField() 
    content = models.TextField()
    def __str__(self):
        return f"{self.title}"