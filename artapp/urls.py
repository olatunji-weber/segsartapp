from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('gallery.html', views.gallery, name='gallery'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about')
]