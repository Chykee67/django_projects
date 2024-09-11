from django.urls import path

from . import views

app_name = 'usr_profile'

urlpatterns = [
    path('<str:user_first_name>', views.IndexView.as_view(), name='index'),
    path('<str:user_first_name>/cart/', views.CartView.as_view(), name='usercart'),
    path('<str:user_first_name>/orders/', views.OrdersView.as_view(), name='userorders'),
    path('<str:user_first_name>/notificatons/', views.NotificationsView.as_view(), name='notifications'),
    path('<str:user_first_name>/edit_user_profile', views.EditUserProfile.as_view(), name='edit_user_profile')
]