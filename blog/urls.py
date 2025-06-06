from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path( '', views.home, name='home'),
    path( 'news/', views.news, name='news'),
    path( 'business/', views.business, name='business'),
    path( 'politics', views.politics, name='politics'),
    path( 'sport', views.sport, name='sport'),
    path( 'post/<slug:slug>', views.post_detail, name='post_detail'),

    path( 'register', views.register, name='register'),


]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)