from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('grocery/', include('grocery.urls')),
    path('account/', include('user_account.urls')),
]
