from django.urls import path, include  # type: ignore
from . import views


# https://youtu.be/ZxMB6Njs3ck?t=2927

app_name = 'item'


urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
]
