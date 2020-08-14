from django.urls import path
from . import views


urlpatterns = [
    path('', views.map, name='map'),
    path('extra/', views.extra, name='extra'),
]
