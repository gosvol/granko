from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('catalog-of-monuments', views.catalog_of_monuments, name='catalog'),
    path('types-of-granite', views.types_of_granite, name='types'),
    path('wholesale-price', views.wholesale_price, name='price'),
    path('construction', views.construction, name='construction'),
    path('album', views.album, name='album'),

]
