from django.contrib import admin
from django.urls import path 
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index', views.index , name ='index'),
    path('thank' , views.thanks , name='thank'),  
    path('' , views.upload_data ,name = "upload_data")
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT);