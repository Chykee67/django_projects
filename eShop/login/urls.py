from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [
    path('', views.myloginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('password_reset', views.PasswordResetView.as_view(), name='password_reset'),
]