from django.contrib import admin
from django.urls import path, include
from . import views
import notifications.urls
from django.conf.urls import url




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('msg/', views.message, name='msg'),
    path('grocery/', include('grocery.urls')),
    path('account/', include('user_account.urls')),
    path('', include('pwa.urls')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('accounts/', include('django.contrib.auth.urls'))
]
