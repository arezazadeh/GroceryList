from django.urls import path
from . import views

app_name = 'user_account'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('find_user/', views.find_user, name='find'),
    path('reset_pass/', views.reset_password, name='reset'),
]
