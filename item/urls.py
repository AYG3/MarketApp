from django.urls import path, include  # type: ignore
from . import views


# https://youtu.be/ZxMB6Njs3ck?t=2927

app_name = 'item' #is the namespace we use in the urls


urlpatterns = [
    path('', views.items, name='browse'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.detail, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]
