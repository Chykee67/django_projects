from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [
    path('', views.SignIn, name='sign_in'),
    path('auth_user/', views.AuthoriseUser, name='auth_user'),
    path('sign_up/', views.SignUp, name='sign_up'),
    path('create_user/', views.CreateUser, name='create_user')
]