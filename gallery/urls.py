from django.urls import path
from . import views
urlpatterns = [
    path('flowers', views.flowers, name='flowers'),
    path('product', views.product, name='product'),
    path('events', views.events, name='events'),
]