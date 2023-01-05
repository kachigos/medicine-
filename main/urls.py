from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('service', service, name='service'),
    path('price', price, name='price'),
    path('contact', contact, name='contact'),
    path('team', team, name='team'),
    path('testimonial', testimonial, name='testimonial'),
    path('appointment', appointment, name='appointment'),
    path('search', search, name='search'),

]