from django.urls import path, include
from .views import login_user, logout_user, register_user

app_name = 'users'

urlpatterns = [
    path('', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('register_user', register_user, name='register'),
]
