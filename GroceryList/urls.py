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
    path('grocery/', include('grocery.urls')),
    path('account/', include('user_account.urls')),
    path('', include('pwa.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

