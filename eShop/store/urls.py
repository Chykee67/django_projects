from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('<str:user_name>/', views.IndexView, name='index'),
]