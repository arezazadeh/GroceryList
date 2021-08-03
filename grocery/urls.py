from django.urls import path
from . import views

app_name = 'grocery'
urlpatterns = [
    path('create_list/', views.create_list, name='create_list'),
    path('add/', views.add_to_list, name='add'),
    path('list/', views.view_list, name='list'),


]
