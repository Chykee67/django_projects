from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [
    path('', views.myloginView.as_view(), name='login'),
    path('logout/', views.LogOutUser, name='logout'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
]