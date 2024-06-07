from django.urls import path
from . import views

# https://youtu.be/ZxMB6Njs3ck - creating user login
app_name='core'

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login')
]
