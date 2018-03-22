__author__ = 'rammanojkumar-j'

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms', views.formret, name='forms'),
    path('test',views.getName,name='test'),
    path('contact',views.getContact,name='contact')
]
