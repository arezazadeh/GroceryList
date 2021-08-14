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
    path('new_item/', views.new_item, name='new_item'),
    path('archived/', views.view_archived, name='archive'),
    path('delete_item/<int:item_id>/', views.delete_item, name='del_item'),
    path('create_menu/', views.create_menu, name='c-menu'),
    path('view_menu/', views.view_menu, name='menu'),
    path('menu_detail/<int:dish_id>/', views.view_menu_detail, name='menu_detail'),
    


]
