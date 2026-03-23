from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('what-we-do/', views.what_we_do, name='what_we_do'),
    path('contact/', views.contact, name='contact'),
    path('pitch-in/', views.pitch_in, name='pitch_in'),
    path('apply/', views.apply, name='apply'),
]

