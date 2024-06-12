from django.contrib.auth import views as auth_views #import as auth_views so it doesn't clash with views
from django.urls import path
from . import views

from .forms import LoginForm
# https://youtu.be/ZxMB6Njs3ck - creating user login
app_name='core'

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView(next_page='/'), name='logout'),
]
