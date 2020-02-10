from django.urls import path
from . import views

app_name = 'phonebook'

urlpatterns = [
    path('', views.index, name='index'),
    path('new.html', views.new, name='new'),
    path('new.html', views.add, name='add')
]