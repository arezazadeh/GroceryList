from django import urls
from django.conf.urls import url
from django.urls import path, include
from . import views





urlpatterns = [
    path('list/<int:pk>/', views.getList),
    path('createlist/', views.createList),

]
