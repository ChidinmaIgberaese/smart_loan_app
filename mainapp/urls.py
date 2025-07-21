from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('apply-loan/', views.apply_loan, name='apply-loan'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('success/', views.loan_success, name='loan_success'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
]
