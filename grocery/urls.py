from django.urls import path
from . import views

app_name = 'grocery'
urlpatterns = [
    path('create_list/', views.create_list, name='create_list'),
    path('add/', views.add_to_list, name='add'),
    path('list/', views.view_list, name='list'),
    path('complete/<int:item_id>/', views.complete, name='complete'),
    path('undo_item/<int:item_id>/', views.undo_item, name='undo'),
    path('delete/', views.delete_list, name='delete'),
    path('new_cat/', views.new_cat, name='new_cat'),
    


]
