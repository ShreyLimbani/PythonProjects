from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'phonebook'

urlpatterns = [
    path('', views.index, name='index'),
    path('new.html', views.new, name='new'),
    url(r'^add/$', views.add, name='add')
]