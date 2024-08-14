from django.urls import path

from . import views

app_name = 'usr_profile'

urlpatterns = [
    path('', views.Index, name='index'),
    path('<str:user_name>/', views.Index, name='profile')
]