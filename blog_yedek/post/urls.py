from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:category_slug>', category_show, name='category_show'),
    path('post/<slug:post_slug>', post_show, name='post_show'),
    path('comment/delete/<int:pk>/', comment_delete, name='comment_delete'),
]