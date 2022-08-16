from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Blog_post, Comment
from .forms import CommentModelForm

def category_show(request, category_slug):
    context = dict()
    ctgry= get_object_or_404(Category, slug=category_slug)
    context['items'] = Blog_post.objects.filter(
        category=ctgry,
        status="published",
    )

    return render(request, 'category.html', context)

def post_show(request, post_slug):
    context = dict()
    context['post']= get_object_or_404(Blog_post, slug=post_slug)
    context['comments']= Comment.objects.filter(
        blog_name=context['post'],
        status="published",
    )
    posts = Blog_post.objects.filter(
        category=context['post'].category,
        status="published",
    )
    context['items'] = posts
    context['related'] = posts[:3]
    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user =request.user
            item.blog_name = context['post']
            item.save()
            context['messages']=["Yorumunuz eklendi."]
        
    return render(request, 'post.html', context)


def comment_delete(request, pk):
    item = Comment.objects.get(pk=pk)
    
    item.status = "deleted"
    item.save()
    return redirect('/hesap/yorumlar')
