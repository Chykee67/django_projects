from django.urls import path

from . import views

app_name = 'login'

urlpatterns = [
    path('', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('sign_up/', views.MySignupView.as_view(), name='sign_up'),
    path('password_reset', views.MyPasswordResetView.as_view(), name='password_reset'),
]