from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('', home, name='home'),
    path('teachers/',teachers, name='teachers'),
    path('meetings/', meetings, name='meetings'),
    path('search/', search_teachers, name='search_teachers'),
]