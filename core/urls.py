from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('your_notes/', views.your_notes, name='your_notes'),
    path('likes/', views.likes, name='likes'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]