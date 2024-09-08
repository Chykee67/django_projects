from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [
    path('', views.myloginView.as_view(), name='login'),
    path('logout/', views.LogOutUser, name='logout'),
    path('sign_up/', views.SignUp, name='sign_up'),
    path('create_user/', views.CreateUser, name='create_user')
]