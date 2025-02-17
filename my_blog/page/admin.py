from django.contrib import admin
from page.models import Page, Message


class PageModify(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status', 
        'updated_at',
        'cover_image',
        'content',
        'sidebar'
    )
    list_filter = ('status', )
    list_editable = (
        'title',
        'status', 
        'content',
        'cover_image',
        'sidebar'
    )

class message_list(admin.ModelAdmin):
    list_display = (
        'pk',
        'user_name',
        'content',
        'subject', 
        'mail',
        'sent_at'
    )
    list_filter = ('mail','subject')
    

admin.site.register(Page, PageModify)
admin.site.register(Message, message_list)