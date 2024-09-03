from django.urls import path

from . import views

app_name = 'usr_profile'

urlpatterns = [
    path('<str:user_first_name>', views.Index, name='profile'),
    path('<str:user_name>/cart/', views.CartView, name='usercart'),
    path('<str:user_name>/orders/', views.OrdersView, name='userorders'),
    path('<str:user_name>/notificatons/', views.Notifications, name='notifications'),
]