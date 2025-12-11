

from django.urls import path
# from app.views import dashboard

# urlpatterns = [
#     path('', dashboard, name='dashboard'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('users/add/', views.add_user, name='add_user'),
    path('users/list/', views.user_list, name='user_list'),
    path('roles/', views.roles, name='roles'),

    path('customers/', views.customers, name='customers'),

    path('products/add/', views.add_product, name='add_product'),
    path('products/list/', views.product_list, name='product_list'),
    path('pos/', views.pos_page, name='pos'),
    path('calender/', views.calender, name='calender'),
    path('update_user/', views.updateuser ,name='update_user'),

]
