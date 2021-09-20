from django.contrib import admin
from django.urls import path, include
from . import views
import notifications.urls
from django.conf.urls import url
from . import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('msg/', views.message, name='msg'),
    path('grocery/', include('grocery.urls')),
    path('account/', include('user_account.urls')),
    path('', include('pwa.urls')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('send_push/', views.send_push, name='send_push'),
    path('webpush/', include('webpush.urls')),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

