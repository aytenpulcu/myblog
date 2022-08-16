from django.urls import path

from .views import sign_in, log_in, log_out,see_cmnt

urlpatterns = [
    path('kayit/', sign_in, name='sign_in'),
    path('giris/', log_in, name='log_in'), 
    path('cikis/', log_out, name='log_out'),
    path('yorumlar/', see_cmnt, name='see_cmnt'),
]