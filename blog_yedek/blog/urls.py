
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from page.views import index, page_show, contact_us, see_all


urlpatterns = [
    path('', index, name='index'), 
    path('admin/', admin.site.urls),
    path('<slug:page_slug>', page_show, name='page_show'),
    path('iletisim/', contact_us, name='contact_us'),
    path('gonderiler/', see_all, name='see_all'),

    path('hesap/', include('page.urls'), ),    #kullanıcı giris ve kayıt sayfaları
    path('blog/', include('post.urls'), ),  # kategori ve post sayfaları
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

