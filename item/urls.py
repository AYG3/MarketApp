from django.urls import path, include
from . import views


# https://youtu.be/ZxMB6Njs3ck?t=2927

app_name = 'item'


urlpatterns = [
    path('<int:pk>/', views.detail, name='detail')
]
