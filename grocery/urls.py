from django.urls import path
from . import views

app_name = 'grocery'
urlpatterns = [
    path('create_list/<int:list_id>/', views.create_list, name='create_list'),
    path('add/<int:list_id>/', views.add_to_list, name='add'),
    path('list/<int:list_id>/', views.view_list, name='list'),
    path('complete/<int:item_id>/<int:list_id>/', views.complete, name='complete'),
    path('custom_item/<int:list_id>/', views.add_custom_item_to_list, name='custom_item'),
    path('undo_item/<int:item_id>/<int:list_id>/', views.undo_item, name='undo'),
    path('delete/', views.delete_list, name='delete'),
    path('new_cat/', views.new_cat, name='new_cat'),
    path('new_item/', views.new_item, name='new_item'),
    path('delete_item/<int:item_id>/<int:list_id>/', views.delete_item, name='del_item'),
    path('create_menu/', views.create_menu, name='c-menu'),
    path('view_menu/', views.view_menu, name='menu'),
    path('menu_detail/<int:dish_id>/', views.view_menu_detail, name='menu_detail'),  
    path('recipe_search/', views.recipe_search, name="recipe_search"),
    path('recipe_detail/<path:recipe_link>/', views.recipe_detail, name="recipe_detail"),
    path('add_recipe/<str:recipe_id>/', views.add_recipe_to_menu, name="add_recipe"),
    path('share_recipe/<str:recipe_id>/', views.share_recipe, name="share"),
    path('create_new_list/', views.create_new_list, name="new_list"),
    path('user_lists/', views.view_lists, name='user_lists'),
    path('delete_list/<int:list_id>/', views.delete_user_list, name='del_user_list'),
    path('delete_menu/<int:menu_id>/', views.delete_menu, name='delete_menu'),
    
    path('discussion/', views.PostListView.as_view(), name='discussion'),
    path('post_detail/<int:post_id>/', views.post_detail, name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/update/<int:post_id>/', views.post_update, name='post-update'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post-delete'),
    
    path('comment/add/<int:post_id>/', views.comment_add, name='comment-add'),
    path('comment/update/<int:comment_id>/<int:post_id>/', views.comment_update, name='comment-update'),
    path('comment/delete/<int:comment_id>/<int:post_id>/', views.delete_comment, name='comment-delete'),
    path('notification/delete/<int:notify_id>/', views.delete_notification, name='notify-delete'),
    
    path('add_favorite_item/<int:item_id>/<str:item_name>/<int:list_id>/', views.favorite_item, name='fav_item'),
    path('remove_favorite_item/<int:item_id>/<str:item_name>/<int:list_id>/', views.remove_fav_item, name='un_fav_item'),
    path('view_fav/', views.view_fav, name='view_fav'),
    path('add_to_fav/', views.add_to_fav, name='add_fav'),
    path('add_fav/', views.add_fav, name='add_to_fav'),
    path('del_fav/<int:item_id>/', views.del_fav, name='del_fav'),
    path('api/', views.api_get),
    
    

]
