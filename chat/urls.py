from django.urls import path
from django.conf.urls import include
from .views import index
from .views import room


app_name='chat'

urlpatterns = [
    path('', index,name='index'),
    path('<str:room_name>/', room, name='room'),
]
