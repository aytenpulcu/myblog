from django.contrib import admin
from .models import Blog_post, Category, Comment

class TextModify(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'image',
        'category',
        'content',
        'status', 
        'updated_at',
        'author',
        'next_img'
    )
    list_filter = ('status', )
    list_editable = (
        'title',
        'status', 
        'image',
        'category',
        'content',
        'next_img',
    )

class CategoryModify(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status', 
        'updated_at',
    )
    list_filter = ('status', )
    list_editable = (
        'title',
        'status', 
    )

class comment_list(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'blog_name',
        'status', 
        'createt_at',
    )
    list_filter = ('status', )
    list_editable = (
        'status', 
        'user',
    )


admin.site.register(Blog_post, TextModify)
admin.site.register(Category, CategoryModify)
admin.site.register(Comment,comment_list)
