from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dark/', views.dashboard_dark, name='dashboard_dark'),
    path('app/', views.frontend_app, name='frontend_app'),
    path('frontend/login/', views.frontend_login, name='frontend_login'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('stores/', views.shop_list, name='shop_list'),
    path('stores/<str:store_type>/', views.store_detail, name='store_detail'),
    path('stores/<str:store_type>/pdf/', views.store_pdf, name='store_pdf'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('report/', views.report_with_proof, name='report_with_proof'),
    path('settings/', views.user_settings, name='user_settings'),
    path('profit/', views.profit, name='profit'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
