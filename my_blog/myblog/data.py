
from post.models import Category, Blog_post
from page.models import Page

def need_data(request):
    context = dict()

    context['categories'] = Category.objects.filter(
        status="published"
    ).order_by('title')

    context['pages'] = Page.objects.filter(
        status="published"
    ).order_by('title')

    context['latest']  = Blog_post.objects.filter(
        status="published"
    )[:4]
    context['posts'] = Blog_post.objects.filter(
        status='published',
    )[:5] 
    #context['latest'] = latest[:4]
    return context 